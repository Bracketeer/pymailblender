import sys
import json
import tinys3

from PyQt5 import QtCore, QtGui, QtWidgets
from clientinfomodal import Ui_ClientInfoModal_2

class clientinfomodalgui(Ui_ClientInfoModal_2):

    def __init__(self, dialog):

        Ui_ClientInfoModal_2.__init__(self)
        self.setupUi(dialog)
        self.SaveBtn.clicked.connect(self.addClientInfo)
        self.CancelBtn.clicked.connect(sys.exit)
        self.data = "data.json"
        self.clientinfo = {}


        try:
            fileObject = open(self.data, "rb")
            self.clientinfo = json.load(fileObject)
            fileObject.close()

        # If no data file is found, return empty dictionary
        except:
            self.clientinfo = {}

    def write(self):
        with open('data.json', mode='a', encoding='utf-8') as fileObject:
            json.dump(self.clientinfo, fileObject)
        fileObject.close()

    # Read Serialized file
    def read(self, data):
        try:
            fileObject = open(self.data, "r")
            self.clientinfo = json.load(fileObject)
            fileObject.close()

        # If no data file is found, return empty dictionary
        except FileNotFoundError:
            self.clientinfo = {}

    def phoneFormat(self, p):
        return format(int(p[:-1]), ",").replace(",", "-") + p[-1]

    def addClientInfo(self, clientinfomodalgui):
        firstName = self.FirstNameInput.text()
        lastName = self.LastNameInput.text()
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
        hexColor = self.HexColorInput.text()

        print(self.clientinfo)
        if len(zip) != 5 and zip.isnumeric() == False:
            print('Please enter a proper zip code')
        elif len(zip) == 5 and zip.isnumeric() == True:
            print(zip)

        if hexColor.startswith('#') and len(hexColor) == 7:
            self.HexColorInput.setStyleSheet("background-color:" + hexColor + ";")
            print(hexColor)

        else:
            hexColor = '#'+hexColor
            self.HexColorInput.setStyleSheet("background-color:" + hexColor + ";")
            print(hexColor)

        if state == 'State':
            print('Please select a State')

        client = self.clientinfo
        name = firstName + ' ' + lastName
        print(name)
        client[name] = {
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
            }

        self.write()
        print(client)
        sys.exit()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()

    prog = clientinfomodalgui(dialog)

    dialog.show()
    sys.exit(app.exec_())