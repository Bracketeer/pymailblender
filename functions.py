import sys
import json

from PyQt5 import QtCore, QtGui, QtWidgets
from mailblender import Ui_MailBlender

class mailblenderGui(Ui_MailBlender):

    def __init__(self, MailBlender):

        Ui_MailBlender.__init__(self)
        self.setupUi(MailBlender)
        self.SaveBtn.clicked.connect(self.addClientInfo)
        self.CancelBtn.clicked.connect(self.clearAddClientFields)
        self.appData = []
        self.data = "data.json"
        try:
            fileObject = open(self.data, "r")
            self.appData = json.load(fileObject)
            print(self.appData)
            fileObject.close()

        # If no data file is found, return empty dictionary
        except FileNotFoundError:
            self.appData = []

    def write(self):
        fileObject = open(self.data, "w")
        json.dump(self.appData, fileObject)
        fileObject.close()

    def addClientInfo(self, mailblenderGui):
        firstName = self.FirstNameInput.text()
        lastName = self.LastNameInput.text()
        fullName = firstName + ' ' + lastName
        companyName = self.CompanyNameInput.text()
        address1 = self.Address1Input.text()
        address2 = self.Address2Input.text()
        city = self.CityInput.text()
        zip = self.ZipInput.text()
        state = self.StateComboBox.currentText()
        email = self.EmailInput.text()
        phone = self.phoneFormat(self.PhoneInput.text())
        blog = self.BlogURLInput.text()
        homeValue = self.HomeValueURLInput.text()
        homeSearch = self.HomeSearchURLInput.text()
        hexColor = self.hexFormat(self.HexColorInput.text())

        self.clientinfo = {fullName:{
            'firstName': firstName,
            'lastName': lastName,
            'companyName': companyName,
            'address1': address1,
            'address2': address2,
            'city': city,
            'zip': zip,
            'state': state,
            'email': email,
            'phone': phone,
            'blog': blog,
            'homeValue': homeValue,
            'homeSearch': homeSearch,
            'hexColor': hexColor
            }}
        print(self.clientinfo)

        self.appData.append(self.clientinfo)
        self.write()
        print(self.appData)

    def clearAddClientFields(self):
        self.FirstNameInput.clear()
        self.LastNameInput.clear()
        self.CompanyNameInput.clear()
        self.Address1Input.clear()
        self.Address2Input.clear()
        self.CityInput.clear()
        self.ZipInput.clear()
        self.StateComboBox.currentText()
        self.EmailInput.clear()
        self.PhoneInput.clear()
        self.BlogURLInput.clear()
        self.HomeValueURLInput.clear()
        self.HomeSearchURLInput.clear()
        self.HexColorInput.clear()
        self.HexColorFrame.setStyleSheet("border: 1px solid rgb(129, 129, 129);")

    def hexFormat(self, hexColor):
        if hexColor.startswith('#') and len(hexColor) == 7:
            self.HexColorFrame.setStyleSheet("QFrame#HexColorFrame{background-color:" + hexColor + ";}")

        else:
            hexColor = '#' + hexColor
            self.HexColorInput.clear()
            self.HexColorInput.insert(hexColor)
            self.HexColorFrame.setStyleSheet("QFrame#HexColorFrame{background-color:" + hexColor + ";}")
            return hexColor

    def phoneFormat(self, p):
        return format(int(p[:-1]), ",").replace(",", "-") + p[-1]

    def stateVerify(self):
        if state == 'State':
            print('Please select a State')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MailBlender = QtWidgets.QMainWindow()
    ui = Ui_MailBlender()
    ui.setupUi(MailBlender)
    prog = mailblenderGui(MailBlender)
    MailBlender.show()
    sys.exit(app.exec_())