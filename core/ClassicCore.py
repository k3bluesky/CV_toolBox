from GUI.Menu import Ui_menu
from GUI.trainClassic import Ui_trainClassic


class classicWindow(Ui_trainClassic, Ui_menu):

    def __init__(self):
        super(classicWindow, self).__init__()
        self.setupUi(self)
