# -*- coding: utf-8 -*-
import numpy as np
from PyQt5.QtCore import pyqtSignal, QThread, QTimer
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QMessageBox, QFileDialog
from tensorflow.keras import models
from tensorflow.keras.preprocessing import image
from GUI.trainWin import Ui_trainWin
from GUI.useModel import Ui_testModel
import cv2
import core.global_data as gl
import tensorflow as tf
class Video():
    def __init__(self, capture):
        self.capture = capture
        self.currentFrame = np.array([])

    def captureFrame(self):
        ret, readFrame = self.capture.read()
        return readFrame

    def captureNextFrame(self):
        ret, readFrame = self.capture.read()
        if (ret == True):
            self.currentFrame = cv2.cvtColor(readFrame, cv2.COLOR_BGR2RGB)

    def convertFrame(self):
        try:
            height, width = self.currentFrame.shape[:2]
            img = QImage(self.currentFrame, width, height, QImage.Format_RGB888)
            img = QPixmap.fromImage(img)
            self.previousFrame = self.currentFrame
            return img
        except:
            return None

class codeThread(QThread):
    # 通过类成员对象定义信号
    update_date = pyqtSignal(str)

    def __init__(self):
        super(codeThread, self).__init__()
        self.count = 0
    # 处理业务逻辑
    def run(self):
        if gl.ret == True:
            self.cameraScreen.setPixmap()

class useModelWindow(Ui_testModel,Ui_trainWin):

    def __init__(self):
        super(useModelWindow, self).__init__()
        self.setupUi(self)

        self.cameraScreen.setPixmap(QPixmap('./img/OIP-C.jpg'))

        self.timer_camera = QTimer()  # 定义定时器，用于控制显示视频的帧率
        self.cap = cv2.VideoCapture()  # 视频流
        self.CAM_NUM = 0  # 为0时表示视频流来自笔记本内置摄像头
        self.openCamera = False

        self.startButton.clicked.connect(self.openC)
        self.startButton.clicked.connect(self.startCamera)
        self.startButton.clicked.connect(self.getXYZ)
        self.timer_camera.timeout.connect(self.show_camera)  # 若定时器结束，则调用show_camera()

        self.pushButton_2.clicked.connect(self.closeCamera)

        self.uploadButton.clicked.connect(self.choosePic)

    def choosePic(self):
        self.getXYZ()
        dir = QFileDialog()
        dir.setNameFilter('图片文件(*.jpg *.png *.bmp *.gif)')
        dir.setFileMode(QFileDialog.ExistingFile)

        dir.setDirectory('..\\')

        if dir.exec_():
            self.picEdit.setText(dir.selectedFiles()[0])
        picPath = self.picEdit.text()
        self.cameraScreen.setPixmap(QPixmap(picPath))
        img = image.load_img(picPath,color_mode = "rgb" ,target_size=(int(gl.designX), int(gl.designY)))
        x = image.img_to_array(img).reshape(1, int(gl.designX), int(gl.designY),
                                          int(gl.designZ))  # 将图片转为数组形式,转为4维数组[样本数,边像素，边像素，通道数]
        # x = 255.0 - x.astype('float32')#图片翻转颜色
        model = models.load_model("./model.h5")
        pre = model.predict(x)  # 应用模型
        y = np.argmax(pre)
        y = np.argmax(pre)
        self.resultEdit.setText(str(y))


    def getXYZ(self):
        if gl.designX == 0:
            gl.designX = self.xlineEdit.text()
        if gl.designY == 0:
            gl.designY = self.ylineEdit_2.text()
        if gl.designZ == 0:
            gl.designZ = self.zlineEdit_3.text()

    def closeCamera(self):
            self.openCamera = False
    def openC(self):
            self.openCamera = True


    def startCamera(self):
        from tensorflow._api.v2.compat import v1
        v1.disable_eager_execution()
        if self.timer_camera.isActive() == False:  # 若定时器未启动

            flag = self.cap.open(self.CAM_NUM)  # 参数是0，表示打开笔记本的内置摄像头，参数是视频文件路径则打开视频
            if flag == False:  # flag表示open()成不成功
                msg = QMessageBox.warning(self, 'warning', "请检查相机于电脑是否连接正确",
                                                    buttons=QMessageBox.Ok)
            else:
                self.timer_camera.start(30)  # 定时器开始计时30ms，结果是每过30ms从摄像头中取一帧显示
        else:
            self.timer_camera.stop()  # 关闭定时器
            self.cap.release()  # 释放视频流
            self.label.clear()  # 清空视频显示区域
            self.label.setText("摄像头在开启的过程中会比较慢，请稍等，别乱点，以免卡死。")

    def show_camera(self):

        model = models.load_model("./model.h5")
        flag, self.image = self.cap.read()  # 从视频流中读取
        #

        if self.openCamera:
            img_raw = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)

            show = img_raw[:, :, ::-1]
        else:
            show = cv2.resize(self.image, (640, 480))  # 把读到的帧的大小重新设置为 640x480
        #

        show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)  # 视频色彩转换回RGB，这样才是现实的颜色
        showImage = QImage(show.data, show.shape[1], show.shape[0],
                                 QImage.Format_RGB888)  # 把读取到的视频数据变成QImage形式

        x = cv2.resize(self.image,(int(gl.designX), int(gl.designY)))
        x = image.img_to_array(x).reshape(1, int(gl.designX), int(gl.designY), int(gl.designZ))  # 将图片转为数组形式,转为4维数组[样本数,边像素，边像素，通道数]
        # x = 255.0 - x.astype('float32')#图片翻转颜色
        pre = model.predict(x)  # 应用模型
        y = np.argmax(pre)


        print(pre)
        self.resultEdit.setText(str(y))
        self.cameraScreen.setPixmap(QPixmap.fromImage(showImage))  # 往显示视频的Label里 显示QImage
