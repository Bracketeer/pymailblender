import sys
import tinys3
from PyQt5 import QtCore, QtGui, QtWidgets
from templateselector import Ui_MainWindow


class templateselectorgui(Ui_MainWindow):
    def __init__(self, mainwindow):
        Ui_MainWindow.__init__(self)
        self.setupUi(mainwindow)
        self.actionAdd_Client.triggered.connect(self.addClient)
        self.HeroImageUploadBtn.clicked.connect(self.addClient)

    def addClient(self, templateselectorgui):
        print('hello')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    prog = templateselectorgui(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
