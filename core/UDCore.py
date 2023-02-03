from GUI.Menu import Ui_menu
from GUI.trainUD import Ui_trainWD

class UDWindow(Ui_trainWD,Ui_menu):

    def __init__(self):
        super(UDWindow, self).__init__()
        self.setupUi(self)