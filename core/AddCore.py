from GUI.design import Ui_design
from GUI.addConv import Ui_AddCon
from GUI.addPooling import Ui_AddPooling
from GUI.addFullConnect import Ui_addFC

class addConvWindow(Ui_AddCon, Ui_design):

    def __init__(self):
        super(addConvWindow, self).__init__()
        self.setupUi(self)


class addPoolingWindow(Ui_AddPooling, Ui_design):

    def __init__(self):
        super(addPoolingWindow, self).__init__()
        self.setupUi(self)

class addFCWindow(Ui_addFC, Ui_design):

    def __init__(self):
        super(addFCWindow, self).__init__()
        self.setupUi(self)
