from GUI.Menu import Ui_menu
from GUI.design import Ui_design
from GUI.trainWin import Ui_trainWin

class trainWindow(Ui_trainWin,Ui_design):

    def __init__(self):
        super(trainWindow, self).__init__()
        self.setupUi(self)

        self.useModel.clicked.connect(self.openUseModel)

    def openUseModel(self):
        import core.useModelCore
        self.design = core.useModelCore.useModelWindow()
        self.design.show()