from GUI.trainWin import Ui_trainWin
from GUI.useModel import Ui_testModel


class useModelWindow(Ui_testModel,Ui_trainWin):

    def __init__(self):
        super(useModelWindow, self).__init__()
        self.setupUi(self)