import sys
import json
import boto3

from PyQt5 import QtCore, QtGui, QtWidgets
from mailblender import Ui_MailBlender

class mailblenderGui(Ui_MailBlender):

    def __init__(self, MailBlender):

        Ui_MailBlender.__init__(self)
        self.setupUi(MailBlender)
        self.SaveBtn.clicked.connect(self.addClientInfo)
        self.CancelBtn.clicked.connect(self.removeClient)
        self.appData = []
        self.s3 = boto3.resource('s3')
        self.s3.Bucket('vyralmarketing').download_file('vyral-marketing/MailBlender/data.json', 'data.json')
        self.data = 'data.json'
        for bucket in self.s3.buckets.all():
            print(bucket.name)
        self.read()

        self.loadClientList()
    def read(self):
        try:
            fileObject = open(self.data, "r")
            self.appData = json.load(fileObject)
            fileObject.close()

        # If no data file is found, return empty list
        except FileNotFoundError:
            self.appData = []

    def write(self):
        fileObject = open(self.data, "w")
        json.dump(self.appData, fileObject, indent=4)
        fileObject.close()
        self.s3.Bucket('vyralmarketing').upload_file('data.json', 'vyral-marketing/MailBlender/data.json')
        print('success')

    def loadClientList(self):
        for c in range(len(self.appData)):
            self.clientListWidget.addItems(self.appData[c])
        self.clientListWidget.currentItemChanged.connect(self.viewClientInfo)
        self.clientListWidget.sortItems()


    def viewClientInfo(self):
        i = self.clientListWidget.currentRow()
        c = self.clientListWidget.currentItem().text()
        clientinfolist = self.appData[i]
        self.clearAddClientFields()
        self.FirstNameInput.insert(clientinfolist[c].get('firstName'))
        self.LastNameInput.insert(clientinfolist[c].get('lastName'))
        self.CompanyNameInput.insert(clientinfolist[c].get('companyName'))
        self.Address1Input.insert(clientinfolist[c].get('address1'))
        self.Address2Input.insert(clientinfolist[c].get('address2'))
        self.CityInput.insert(clientinfolist[c].get('city'))
        self.ZipInput.insert(clientinfolist[c].get('zip'))
        # self.StateComboBox.currentText(clientinfolist[c].get('state'))
        self.EmailInput.insert(clientinfolist[c].get('email'))
        self.PhoneInput.insert(clientinfolist[c].get('phone'))
        self.WebsiteURLInput.insert(clientinfolist[c].get('website'))
        self.BlogURLInput.insert(clientinfolist[c].get('blog'))
        self.HomeSearchURLInput.insert(clientinfolist[c].get('homeSearch'))
        self.HomeValueURLInput.insert(clientinfolist[c].get('homeValue'))
        self.HexColorInput.insert(clientinfolist[c].get('hexColor'))
        hexColor = self.HexColorInput.text()
        self.HexColorFrame.setStyleSheet("QFrame#HexColorFrame{background-color:" + hexColor + ";}")
        self.MarketAreaInput.insert(clientinfolist[c].get('marketArea'))

    def removeClient(self):
        i = self.clientListWidget.currentRow()
        c = self.clientListWidget.currentItem().text()
        print(self.appData[i])
        del self.appData[i]
        print(self.appData)
        self.write()


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
        website = self.WebsiteURLInput.text()
        blog = self.BlogURLInput.text()
        homeValue = self.HomeValueURLInput.text()
        homeSearch = self.HomeSearchURLInput.text()
        hexColor = self.hexFormat(self.HexColorInput.text())
        marketArea = self.MarketAreaInput.text()

        self.clientinfo = {
            fullName:
            {
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
            'website': website,
            'blog': blog,
            'homeValue': homeValue,
            'homeSearch': homeSearch,
            'hexColor': hexColor,
            'marketArea': marketArea
            }
        }
        self.s3.Bucket('vyralmarketing').download_file('vyral-marketing/MailBlender/data.json', 'data.json')
        del self.appData[:]
        self.loadClientList()
        self.read()
        self.appData.append(self.clientinfo)
        self.write()
        self.clientListWidget.addItems(self.clientinfo)
        self.clientListWidget.sortItems()
        self.clearAddClientFields()


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
        self.WebsiteURLInput.clear()
        self.BlogURLInput.clear()
        self.HomeValueURLInput.clear()
        self.HomeSearchURLInput.clear()
        self.HexColorInput.clear()
        self.MarketAreaInput.clear()
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
        try:
            return format(int(p[:-1]), ",").replace(",", "-") + p[-1]
        except ValueError:
            print(p)

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