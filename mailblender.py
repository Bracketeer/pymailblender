# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mailblender.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MailBlender(object):
    def setupUi(self, MailBlender):
        MailBlender.setObjectName("MailBlender")
        MailBlender.resize(1175, 814)
        MailBlender.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MailBlender)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.MainContentWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.MainContentWidget.setStyleSheet("QLineEdit{\n"
"padding: 0 10px;\n"
"}")
        self.MainContentWidget.setObjectName("MainContentWidget")
        self.AddClientPage = QtWidgets.QWidget()
        self.AddClientPage.setObjectName("AddClientPage")
        self.StateComboBox = QtWidgets.QComboBox(self.AddClientPage)
        self.StateComboBox.setGeometry(QtCore.QRect(728, 258, 141, 36))
        self.StateComboBox.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.StateComboBox.setFont(font)
        self.StateComboBox.setObjectName("StateComboBox")
        self.StateComboBox.addItem("")
        self.StateComboBox.addItem("")
        self.StateComboBox.addItem("")
        self.StateComboBox.addItem("")
        self.StateComboBox.addItem("")
        self.StateComboBox.addItem("")
        self.StateComboBox.addItem("")
        self.StateComboBox.addItem("")
        self.StateComboBox.addItem("")
        self.StateComboBox.addItem("")
        self.StateComboBox.addItem("")
        self.StateComboBox.addItem("")
        self.StateComboBox.addItem("")
        self.StateComboBox.addItem("")
        self.StateComboBox.addItem("")
        self.StateComboBox.addItem("")
        self.StateComboBox.addItem("")
        self.StateComboBox.addItem("")
        self.StateComboBox.addItem("")
        self.StateComboBox.addItem("")
        self.StateComboBox.addItem("")
        self.StateComboBox.addItem("")
        self.StateComboBox.addItem("")
        self.StateComboBox.addItem("")
        self.StateComboBox.addItem("")
        self.StateComboBox.addItem("")
        self.StateComboBox.addItem("")
        self.StateComboBox.addItem("")
        self.StateComboBox.addItem("")
        self.StateComboBox.addItem("")
        self.StateComboBox.addItem("")
        self.StateComboBox.addItem("")
        self.StateComboBox.addItem("")
        self.StateComboBox.addItem("")
        self.StateComboBox.addItem("")
        self.StateComboBox.addItem("")
        self.StateComboBox.addItem("")
        self.StateComboBox.addItem("")
        self.StateComboBox.addItem("")
        self.StateComboBox.addItem("")
        self.StateComboBox.addItem("")
        self.StateComboBox.addItem("")
        self.StateComboBox.addItem("")
        self.StateComboBox.addItem("")
        self.StateComboBox.addItem("")
        self.StateComboBox.addItem("")
        self.StateComboBox.addItem("")
        self.StateComboBox.addItem("")
        self.StateComboBox.addItem("")
        self.StateComboBox.addItem("")
        self.StateComboBox.addItem("")
        self.HomeSearchURLInput = QtWidgets.QLineEdit(self.AddClientPage)
        self.HomeSearchURLInput.setGeometry(QtCore.QRect(278, 394, 211, 36))
        self.HomeSearchURLInput.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.HomeSearchURLInput.setFont(font)
        self.HomeSearchURLInput.setText("")
        self.HomeSearchURLInput.setObjectName("HomeSearchURLInput")
        self.PhoneInput = QtWidgets.QLineEdit(self.AddClientPage)
        self.PhoneInput.setGeometry(QtCore.QRect(278, 122, 291, 36))
        self.PhoneInput.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PhoneInput.setFont(font)
        self.PhoneInput.setText("")
        self.PhoneInput.setObjectName("PhoneInput")
        self.BlogURLInput = QtWidgets.QLineEdit(self.AddClientPage)
        self.BlogURLInput.setGeometry(QtCore.QRect(578, 348, 291, 36))
        self.BlogURLInput.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.BlogURLInput.setFont(font)
        self.BlogURLInput.setText("")
        self.BlogURLInput.setObjectName("BlogURLInput")
        self.HomeValueURLInput = QtWidgets.QLineEdit(self.AddClientPage)
        self.HomeValueURLInput.setGeometry(QtCore.QRect(498, 394, 221, 36))
        self.HomeValueURLInput.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.HomeValueURLInput.setFont(font)
        self.HomeValueURLInput.setText("")
        self.HomeValueURLInput.setObjectName("HomeValueURLInput")
        self.ZipInput = QtWidgets.QLineEdit(self.AddClientPage)
        self.ZipInput.setGeometry(QtCore.QRect(578, 258, 141, 36))
        self.ZipInput.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ZipInput.setFont(font)
        self.ZipInput.setText("")
        self.ZipInput.setObjectName("ZipInput")
        self.EmailInput = QtWidgets.QLineEdit(self.AddClientPage)
        self.EmailInput.setGeometry(QtCore.QRect(578, 122, 291, 36))
        self.EmailInput.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.EmailInput.setFont(font)
        self.EmailInput.setText("")
        self.EmailInput.setObjectName("EmailInput")
        self.LastNameInput = QtWidgets.QLineEdit(self.AddClientPage)
        self.LastNameInput.setGeometry(QtCore.QRect(578, 30, 291, 36))
        self.LastNameInput.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.LastNameInput.setFont(font)
        self.LastNameInput.setText("")
        self.LastNameInput.setObjectName("LastNameInput")
        self.CityInput = QtWidgets.QLineEdit(self.AddClientPage)
        self.CityInput.setGeometry(QtCore.QRect(278, 258, 291, 36))
        self.CityInput.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.CityInput.setFont(font)
        self.CityInput.setText("")
        self.CityInput.setObjectName("CityInput")
        self.Address1Input = QtWidgets.QLineEdit(self.AddClientPage)
        self.Address1Input.setGeometry(QtCore.QRect(278, 212, 291, 36))
        self.Address1Input.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Address1Input.setFont(font)
        self.Address1Input.setText("")
        self.Address1Input.setObjectName("Address1Input")
        self.Address2Input = QtWidgets.QLineEdit(self.AddClientPage)
        self.Address2Input.setGeometry(QtCore.QRect(578, 212, 291, 36))
        self.Address2Input.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Address2Input.setFont(font)
        self.Address2Input.setText("")
        self.Address2Input.setObjectName("Address2Input")
        self.CompanyNameInput = QtWidgets.QLineEdit(self.AddClientPage)
        self.CompanyNameInput.setGeometry(QtCore.QRect(278, 76, 591, 36))
        self.CompanyNameInput.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.CompanyNameInput.setFont(font)
        self.CompanyNameInput.setText("")
        self.CompanyNameInput.setObjectName("CompanyNameInput")
        self.FirstNameInput = QtWidgets.QLineEdit(self.AddClientPage)
        self.FirstNameInput.setGeometry(QtCore.QRect(278, 30, 291, 36))
        self.FirstNameInput.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.FirstNameInput.setFont(font)
        self.FirstNameInput.setText("")
        self.FirstNameInput.setProperty("clearButtonEnabled", False)
        self.FirstNameInput.setObjectName("FirstNameInput")
        self.WebsiteURLInput = QtWidgets.QLineEdit(self.AddClientPage)
        self.WebsiteURLInput.setGeometry(QtCore.QRect(278, 348, 291, 36))
        self.WebsiteURLInput.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.WebsiteURLInput.setFont(font)
        self.WebsiteURLInput.setText("")
        self.WebsiteURLInput.setObjectName("WebsiteURLInput")
        self.WebLabel = QtWidgets.QLabel(self.AddClientPage)
        self.WebLabel.setGeometry(QtCore.QRect(277, 318, 101, 18))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.WebLabel.setFont(font)
        self.WebLabel.setScaledContents(False)
        self.WebLabel.setObjectName("WebLabel")
        self.ContactLabel = QtWidgets.QLabel(self.AddClientPage)
        self.ContactLabel.setGeometry(QtCore.QRect(277, 0, 191, 18))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ContactLabel.setFont(font)
        self.ContactLabel.setScaledContents(False)
        self.ContactLabel.setObjectName("ContactLabel")
        self.AddressLAbel = QtWidgets.QLabel(self.AddClientPage)
        self.AddressLAbel.setGeometry(QtCore.QRect(277, 182, 101, 18))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.AddressLAbel.setFont(font)
        self.AddressLAbel.setScaledContents(False)
        self.AddressLAbel.setObjectName("AddressLAbel")
        self.HeaderLogoLabel = QtWidgets.QLabel(self.AddClientPage)
        self.HeaderLogoLabel.setGeometry(QtCore.QRect(888, -10, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.HeaderLogoLabel.setFont(font)
        self.HeaderLogoLabel.setScaledContents(False)
        self.HeaderLogoLabel.setObjectName("HeaderLogoLabel")
        self.FooterLogoLabel = QtWidgets.QLabel(self.AddClientPage)
        self.FooterLogoLabel.setGeometry(QtCore.QRect(890, 290, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.FooterLogoLabel.setFont(font)
        self.FooterLogoLabel.setScaledContents(False)
        self.FooterLogoLabel.setObjectName("FooterLogoLabel")
        self.BannerImageLabel = QtWidgets.QLabel(self.AddClientPage)
        self.BannerImageLabel.setGeometry(QtCore.QRect(280, 440, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.BannerImageLabel.setFont(font)
        self.BannerImageLabel.setScaledContents(False)
        self.BannerImageLabel.setObjectName("BannerImageLabel")
        self.HexColorFrame = QtWidgets.QFrame(self.AddClientPage)
        self.HexColorFrame.setGeometry(QtCore.QRect(728, 394, 141, 36))
        self.HexColorFrame.setAutoFillBackground(False)
        self.HexColorFrame.setStyleSheet("QFrame#HexColorFrame{\n"
"border: 1px solid rgb(129, 129, 129);\n"
"}")
        self.HexColorFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.HexColorFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.HexColorFrame.setObjectName("HexColorFrame")
        self.HexColorInput = QtWidgets.QLineEdit(self.HexColorFrame)
        self.HexColorInput.setGeometry(QtCore.QRect(0, 0, 101, 36))
        self.HexColorInput.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.HexColorInput.setFont(font)
        self.HexColorInput.setAutoFillBackground(False)
        self.HexColorInput.setStyleSheet("")
        self.HexColorInput.setText("")
        self.HexColorInput.setObjectName("HexColorInput")
        self.clientListWidget = QtWidgets.QListWidget(self.AddClientPage)
        self.clientListWidget.setGeometry(QtCore.QRect(5, 76, 256, 571))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.clientListWidget.setFont(font)
        self.clientListWidget.setObjectName("clientListWidget")
        self.ClientListLabel = QtWidgets.QLabel(self.AddClientPage)
        self.ClientListLabel.setGeometry(QtCore.QRect(6, 0, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ClientListLabel.setFont(font)
        self.ClientListLabel.setScaledContents(False)
        self.ClientListLabel.setObjectName("ClientListLabel")
        self.searchBoxInput = QtWidgets.QLineEdit(self.AddClientPage)
        self.searchBoxInput.setGeometry(QtCore.QRect(6, 30, 255, 38))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.searchBoxInput.setFont(font)
        self.searchBoxInput.setObjectName("searchBoxInput")
        self.MainContentWidget.addWidget(self.AddClientPage)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.MainContentWidget.addWidget(self.page_2)
        self.verticalLayout.addWidget(self.MainContentWidget)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(0, 50))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.SaveBtn = QtWidgets.QPushButton(self.frame)
        self.SaveBtn.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.SaveBtn.setFont(font)
        self.SaveBtn.setStyleSheet("QPushButton#SaveBtn{\n"
"padding:10px 30px;\n"
"}")
        self.SaveBtn.setFlat(False)
        self.SaveBtn.setObjectName("SaveBtn")
        self.gridLayout.addWidget(self.SaveBtn, 0, 1, 1, 1)
        self.CancelBtn = QtWidgets.QPushButton(self.frame)
        self.CancelBtn.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.CancelBtn.setFont(font)
        self.CancelBtn.setStyleSheet("QPushButton#CancelBtn{\n"
"padding:10px 30px;\n"
"}")
        self.CancelBtn.setObjectName("CancelBtn")
        self.gridLayout.addWidget(self.CancelBtn, 0, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        MailBlender.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MailBlender)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1175, 30))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MailBlender.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MailBlender)
        self.statusbar.setObjectName("statusbar")
        MailBlender.setStatusBar(self.statusbar)
        self.actionAdd_Client = QtWidgets.QAction(MailBlender)
        self.actionAdd_Client.setObjectName("actionAdd_Client")
        self.actionQuit = QtWidgets.QAction(MailBlender)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionAdd_Client)
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MailBlender)
        self.MainContentWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MailBlender)
        MailBlender.setTabOrder(self.FirstNameInput, self.LastNameInput)
        MailBlender.setTabOrder(self.LastNameInput, self.CompanyNameInput)
        MailBlender.setTabOrder(self.CompanyNameInput, self.PhoneInput)
        MailBlender.setTabOrder(self.PhoneInput, self.EmailInput)
        MailBlender.setTabOrder(self.EmailInput, self.Address1Input)
        MailBlender.setTabOrder(self.Address1Input, self.Address2Input)
        MailBlender.setTabOrder(self.Address2Input, self.CityInput)
        MailBlender.setTabOrder(self.CityInput, self.ZipInput)
        MailBlender.setTabOrder(self.ZipInput, self.StateComboBox)
        MailBlender.setTabOrder(self.StateComboBox, self.WebsiteURLInput)
        MailBlender.setTabOrder(self.WebsiteURLInput, self.BlogURLInput)
        MailBlender.setTabOrder(self.BlogURLInput, self.HomeSearchURLInput)
        MailBlender.setTabOrder(self.HomeSearchURLInput, self.HomeValueURLInput)
        MailBlender.setTabOrder(self.HomeValueURLInput, self.HexColorInput)
        MailBlender.setTabOrder(self.HexColorInput, self.SaveBtn)
        MailBlender.setTabOrder(self.SaveBtn, self.CancelBtn)

    def retranslateUi(self, MailBlender):
        _translate = QtCore.QCoreApplication.translate
        MailBlender.setWindowTitle(_translate("MailBlender", "MailBlender"))
        self.StateComboBox.setItemText(0, _translate("MailBlender", "State"))
        self.StateComboBox.setItemText(1, _translate("MailBlender", "Alabama"))
        self.StateComboBox.setItemText(2, _translate("MailBlender", "Alaska"))
        self.StateComboBox.setItemText(3, _translate("MailBlender", "Arizona"))
        self.StateComboBox.setItemText(4, _translate("MailBlender", "Arkansas"))
        self.StateComboBox.setItemText(5, _translate("MailBlender", "California"))
        self.StateComboBox.setItemText(6, _translate("MailBlender", "Colorado"))
        self.StateComboBox.setItemText(7, _translate("MailBlender", "Connecticut"))
        self.StateComboBox.setItemText(8, _translate("MailBlender", "Delaware"))
        self.StateComboBox.setItemText(9, _translate("MailBlender", "Florida"))
        self.StateComboBox.setItemText(10, _translate("MailBlender", "Georgia"))
        self.StateComboBox.setItemText(11, _translate("MailBlender", "Hawaii"))
        self.StateComboBox.setItemText(12, _translate("MailBlender", "Idaho"))
        self.StateComboBox.setItemText(13, _translate("MailBlender", "Illinois"))
        self.StateComboBox.setItemText(14, _translate("MailBlender", "Indiana"))
        self.StateComboBox.setItemText(15, _translate("MailBlender", "Iowa"))
        self.StateComboBox.setItemText(16, _translate("MailBlender", "Kansas"))
        self.StateComboBox.setItemText(17, _translate("MailBlender", "Kentucky"))
        self.StateComboBox.setItemText(18, _translate("MailBlender", "Louisiana"))
        self.StateComboBox.setItemText(19, _translate("MailBlender", "Maine"))
        self.StateComboBox.setItemText(20, _translate("MailBlender", "Maryland"))
        self.StateComboBox.setItemText(21, _translate("MailBlender", "Massachusetts"))
        self.StateComboBox.setItemText(22, _translate("MailBlender", "Michigan"))
        self.StateComboBox.setItemText(23, _translate("MailBlender", "Minnesota"))
        self.StateComboBox.setItemText(24, _translate("MailBlender", "Mississippi"))
        self.StateComboBox.setItemText(25, _translate("MailBlender", "Missouri"))
        self.StateComboBox.setItemText(26, _translate("MailBlender", "Montana"))
        self.StateComboBox.setItemText(27, _translate("MailBlender", "Nebraska"))
        self.StateComboBox.setItemText(28, _translate("MailBlender", "Nevada"))
        self.StateComboBox.setItemText(29, _translate("MailBlender", "New Hampshire"))
        self.StateComboBox.setItemText(30, _translate("MailBlender", "New Jersey"))
        self.StateComboBox.setItemText(31, _translate("MailBlender", "New Mexico"))
        self.StateComboBox.setItemText(32, _translate("MailBlender", "New York"))
        self.StateComboBox.setItemText(33, _translate("MailBlender", "North Carolina"))
        self.StateComboBox.setItemText(34, _translate("MailBlender", "North Dakota"))
        self.StateComboBox.setItemText(35, _translate("MailBlender", "Ohio"))
        self.StateComboBox.setItemText(36, _translate("MailBlender", "Oklahoma"))
        self.StateComboBox.setItemText(37, _translate("MailBlender", "Oregon"))
        self.StateComboBox.setItemText(38, _translate("MailBlender", "Pennsylvania"))
        self.StateComboBox.setItemText(39, _translate("MailBlender", "Rhode Island"))
        self.StateComboBox.setItemText(40, _translate("MailBlender", "South Carolina"))
        self.StateComboBox.setItemText(41, _translate("MailBlender", "South Dakota"))
        self.StateComboBox.setItemText(42, _translate("MailBlender", "Tennessee"))
        self.StateComboBox.setItemText(43, _translate("MailBlender", "Texas"))
        self.StateComboBox.setItemText(44, _translate("MailBlender", "Utah"))
        self.StateComboBox.setItemText(45, _translate("MailBlender", "Vermont"))
        self.StateComboBox.setItemText(46, _translate("MailBlender", "Virginia"))
        self.StateComboBox.setItemText(47, _translate("MailBlender", "Washington"))
        self.StateComboBox.setItemText(48, _translate("MailBlender", "West Virginia"))
        self.StateComboBox.setItemText(49, _translate("MailBlender", "Wisconsin"))
        self.StateComboBox.setItemText(50, _translate("MailBlender", "Wyoming"))
        self.HomeSearchURLInput.setPlaceholderText(_translate("MailBlender", "Home Search URL"))
        self.PhoneInput.setPlaceholderText(_translate("MailBlender", "Phone"))
        self.BlogURLInput.setPlaceholderText(_translate("MailBlender", "Blog URL"))
        self.HomeValueURLInput.setPlaceholderText(_translate("MailBlender", "Home Value URL"))
        self.ZipInput.setPlaceholderText(_translate("MailBlender", "Zip"))
        self.EmailInput.setPlaceholderText(_translate("MailBlender", "Email"))
        self.LastNameInput.setPlaceholderText(_translate("MailBlender", "Last Name"))
        self.CityInput.setPlaceholderText(_translate("MailBlender", "City"))
        self.Address1Input.setPlaceholderText(_translate("MailBlender", "Address 1"))
        self.Address2Input.setPlaceholderText(_translate("MailBlender", "Address 2"))
        self.CompanyNameInput.setPlaceholderText(_translate("MailBlender", "Company Name"))
        self.FirstNameInput.setPlaceholderText(_translate("MailBlender", "First Name"))
        self.WebsiteURLInput.setPlaceholderText(_translate("MailBlender", "Website URL"))
        self.WebLabel.setText(_translate("MailBlender", "Web"))
        self.ContactLabel.setText(_translate("MailBlender", "Contact"))
        self.AddressLAbel.setText(_translate("MailBlender", "Address"))
        self.HeaderLogoLabel.setText(_translate("MailBlender", "Header Logo"))
        self.FooterLogoLabel.setText(_translate("MailBlender", "Footer  Logo"))
        self.BannerImageLabel.setText(_translate("MailBlender", "Banner Image"))
        self.HexColorInput.setPlaceholderText(_translate("MailBlender", "Hex Color"))
        self.ClientListLabel.setText(_translate("MailBlender", "Client List"))
        self.searchBoxInput.setPlaceholderText(_translate("MailBlender", "Search"))
        self.SaveBtn.setText(_translate("MailBlender", "Save"))
        self.CancelBtn.setText(_translate("MailBlender", "Cancel"))
        self.menuFile.setTitle(_translate("MailBlender", "File"))
        self.actionAdd_Client.setText(_translate("MailBlender", "Add Client"))
        self.actionQuit.setText(_translate("MailBlender", "Quit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MailBlender = QtWidgets.QMainWindow()
    ui = Ui_MailBlender()
    ui.setupUi(MailBlender)
    MailBlender.show()
    sys.exit(app.exec_())

