import sys
import pickle
import tinys3
from PyQt5 import QtCore, QtGui, QtWidgets
from clientinfomodal import Ui_ClientInfoModal_2

class clientinfomodalgui(Ui_ClientInfoModal_2):

    def __init__(self, dialog):

        Ui_ClientInfoModal_2.__init__(self)
        self.setupUi(dialog)
        self.SaveBtn.clicked.connect(self.addClientInfo)
        self.CancelBtn.clicked.connect(sys.exit)
        self.data = "data.dat"
        self.clientinfo = {}


        try:
            fileObject = open(self.data, "rb")
            self.clientinfo = pickle.load(fileObject)
            fileObject.close()

        # If no data file is found, return empty dictionary
        except:
            self.clientinfo = {}

    def write(self):
        fileObject = open(self.data, "wb")
        pickle.dump(self.clientinfo, fileObject)
        fileObject.close()

    # Read Serialized file
    def read(self, data):
        try:
            fileObject = open(self.data, "rb")
            self.clientinfo = pickle.load(fileObject)
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
        validatezip = 0
        validatehex = 0
        validatestate = 0

        print(self.clientinfo)
        if len(zip) != 5 and zip.isnumeric() == False:
            print('Please enter a proper zip code')
        elif len(zip) == 5 and zip.isnumeric() == True:
            print(zip)
            validatezip = 1

        if hexColor.startswith('#') and len(hexColor) == 7:
            self.HexColorInput.setStyleSheet("background-color:" + hexColor + ";")
            print(hexColor)

        else:
            hexColor = '#'+hexColor
            self.HexColorInput.setStyleSheet("background-color:" + hexColor + ";")
            print(hexColor)

        if len(hexColor) == 7:
            print(hexColor)
            validatehex = 1


        if state == 'State':
            print('Please select a State')
        else:
           validatestate = 1

        validateall = validatestate + validatehex + validatezip
        if validateall != 10:
            client = self.clientinfo
            name = firstName + '_' + lastName
            print(validateall)
            print(name)
            client[name] = {firstName, lastName, companyName, address1, address2, city, zip, state, email, phone, blog, homeValue, homeSearch, hexColor}
            self.write()
            print(client)
            sys.exit()



if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	dialog = QtWidgets.QDialog()

	prog = clientinfomodalgui(dialog)

	dialog.show()
	sys.exit(app.exec_())