import sys
import tinys3
from PyQt5 import QtCore, QtGui, QtWidgets
from templateselector import Ui_MainWindow
from clientInfoModalFunctions import Ui_ClientInfoModal_2

class templateselectorgui(Ui_MainWindow, Ui_ClientInfoModal_2):
    def __init__(self, mainwindow):
        Ui_MainWindow.__init__(self)
        self.setupUi(mainwindow)
        self.actionAdd_Client.triggered.connect(self.clientinfomodalgui)
        self.HeroImageUploadBtn.clicked.connect(self.addClient)

    def addClient(self, templateselectorgui):
        print('hello')

    class clientinfomodalgui(Ui_ClientInfoModal_2):
        def __init__(self, dialog):
            Ui_ClientInfoModal_2.__init__(self)
            self.setupUi(dialog)
            self.SaveBtn.clicked.connect(self.addClientInfo)
            self.CancelBtn.clicked.connect(sys.exit)
            self.data = "data.json"
            self.clientinfo = {}
            app = QtWidgets.QApplication(sys.argv)
            dialog = QtWidgets.QDialog()
            prog = clientinfomodalgui(dialog)
            dialog.show()
            sys.exit(app.exec_())



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    prog = templateselectorgui(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
