import requests
import re
import os
import time

from tensorflow.keras.preprocessing import image
from PyQt5.QtWidgets import QFileDialog,QMessageBox
import core.global_data as gl
from GUI.Menu import Ui_menu
from GUI.datasetTool import Ui_toolBoxWindow
from PyQt5.QtCore import QThread, pyqtSignal, QObject

class BackendThread(QThread):
    # 通过类成员对象定义信号
    update_date = pyqtSignal(str)

    def __init__(self):
        super(BackendThread, self).__init__()
        self.count = 0
    # 处理业务逻辑
    def run(self):
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400QQBrowser/10.5.3863.400',

        }

        n = 1
        p = 1
        img_num = int(gl.img_num)
        dir_name = gl.img_name  # 生成文件夹
        if not os.path.exists(gl.savePath + '/' + dir_name):
            os.mkdir(gl.savePath + '/' + dir_name)
        time.sleep(2)
        while p <= img_num:
            page = p * 48  # 一页48张图片

            url = 'https://pic.sogou.com/napi/pc/searchList?mode=1&start={}&xml_len=48&query={}'.format(page, gl.img_name)
            if (img_num >= 1): p += 1
            response = requests.get(url, headers=headers)
            plt = re.findall(r'\"picUrl\"\:\".*?\"', response.text)  # response.text是以unicode返回响应的内容
            print(plt)
            for i in plt:
                pic_url = i.split(':')[2][0:-1]
                pic_name = gl.savePath + '/' + dir_name + '/' + str(n) + '.jpg'
                pic_url = re.sub(r'\\u002F', '/', pic_url)
                if (pic_url[-4:] != '.jpg' and pic_url[-4:] != '.png' and pic_url[-5:] != '.jpeg'): continue
                try:
                    result_pic = requests.get('http:' + pic_url, headers=headers)
                except:
                    continue
                # 存入文件，注意使用二进制存储(wb+),b是二进制存储，所有多媒体(图片、音乐、视频)文件都是二进制

                with open(pic_name, 'wb+') as f:
                    f.write(result_pic.content)
                print(pic_name + "downloading........")
                self.update_date.emit(str(pic_name + "downloading........"))
                n += 1
        print('end', "success!")
        self.update_date.emit(str("checking file....."))
        folder_path = gl.savePath + '/' + dir_name  # 将路径替换为您要检查的文件夹的路径

        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                file_size = os.path.getsize(file_path)
                if file_size < 1024:
                    os.remove(file_path)
                    self.update_date.emit(str(f"已删除文件：{file_path}"))

        self.update_date.emit(str("download seccess!"))


class datasetToolWindow(Ui_toolBoxWindow,Ui_menu):

    def __init__(self):
        super(datasetToolWindow, self).__init__()
        self.setupUi(self)

        self.openPathButton.clicked.connect(self.openDatasetPath)
        self.downloadButton.clicked.connect(self.downloadPic)

        self.openPathButton_2.clicked.connect(self.openPicPath)
        self.startButton.clicked.connect(self.startProgram)

    def startProgram(self):
        datagen = image.ImageDataGenerator(
            rotation_range=15,
            width_shift_range=0.1,
            height_shift_range=0.1,
            rescale=1. / 255,
            shear_range=0.2,
            zoom_range=0.2,
            brightness_range=(0.6, 1.4),
            horizontal_flip=True,
            vertical_flip=True,
            fill_mode='nearest')
        source_path = self.picLineEdit.text()
        gl.designX = self.xlineEdit.text()
        gl.designY = self.ylineEdit_2.text()
        gl.designZ = self.zlineEdit_3.text()
        # 遍历源文件夹中的所有文件
        result = []
        for file in os.listdir(source_path):
            # 提取包含扩展名的文件名
            file_name = os.path.basename(file)
            # 拼接源文件路径和文件名
            source_file = source_path+"/"+file_name
            result.append(source_file)

        for i in result:
            img = image.load_img(i, target_size=(int(gl.designX), int(gl.designY)))
            x = image.img_to_array(img)
            print(x.shape)
            x = x.reshape(1, int(gl.designX), int(gl.designY), int(gl.designZ))
            print(x.shape)
            max = 9
            batchs = datagen.flow(x,
                            batch_size=max,
                            save_to_dir=source_path,
                            save_prefix='image',
                            save_format='jpeg')
            j=1
            for batch in batchs:
                augImage = batch[0]
                if j >= 9:
                    break
                j = j + 1
        QMessageBox.information(None,'成功！','增强后的图像已生成到所在文件夹',QMessageBox.Ok)


    def openPicPath(self):
        dir = QFileDialog()
        dir.setFileMode(QFileDialog.DirectoryOnly)
        dir.setDirectory('..\\')

        if dir.exec_():
            self.picLineEdit.setText(dir.selectedFiles()[0])

    def updateForm(self,data):
        self.stepScreen.append(data)

    def openDatasetPath(self):
        dir = QFileDialog()
        dir.setFileMode(QFileDialog.DirectoryOnly)
        dir.setDirectory('..\\')

        if dir.exec_():
            self.pathLineEdit.setText(dir.selectedFiles()[0])

    def downloadPic(self):
        gl.img_name = self.keywordLineEdit.text()
        gl.img_num = self.pageLineEdit.text()
        gl.savePath = self.pathLineEdit.text()
        self.backend = BackendThread()
        self.backend.update_date.connect(self.updateForm)
        self.backend.start()