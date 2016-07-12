class Client:
    def __init__(self, n, f, l, cn, a1, a2, c, z, s, e, p, b, hv, hs, hc):
        self.__FullName = n
        self.__FirstName = f
        self.__LastName = l
        self.__CompanyName = cn
        self.__Address1 = a1
        self.__Address2 = a2
        self.__City = c
        self.__Zip = z
        self.__State = s
        self.__Email = e
        self.__Phone = p
        self.__Blog = b
        self.__HomeValue = hv
        self.__HomeSearch = hs
        self.__HexColor = hc

        def getFullName(self):
            return self.__FullName

        def setFullName(self, n):
            self.__FullName = n

        def getFirstName(self):
            return self.__FirstName

        def setFirstName(self, f):
            self.__FirstName = f

        def getLastName(self):
            return self.__LastName

        def setLastName(self, l):
            self.__LastName = l

        def getCompanyName(self):
            return self.__CompanyName

        def setCompanyName(self, cn):
            self.__CompanyName = cn

        def getAddress1(self):
            return self.__Address1

        def setAddress1(self, a1):
            self.__Address1 = a1

        def getAddress2(self):
            return self.__Address2

        def setAddress2(self, a2):
            self.__Address2 = a2

        def getCity(self):
            return self.__City

        def setCity(self, c):
            self.__City = c

        def getZip(self):
            return self.__Zip

        def setZip(self, z):
            self.__Zip = z

        def getState(self):
            return self.__State

        def setState(self, s):
            self.__State = s

        def getEmail(self):
            return self.__Email

        def setEmail(self, e):
            self.__Email = e

        def getPhone(self):
            return self.__Phone

        def setPhone(self, p):
            self.__Phone = p

        def getHomeValue(self):
            return self.__HomeValue

        def setHomeValue(self, hv):
            self.__HomeValue = hv

        def getHomeSearch(self):
            return self.__HomeSearch

        def setHomeSearch(self, hs):
            self.__HomeSearch = hs

        def getHexColor(self):
            return self.__HexColor

        def setHexColor(self, hc):
            self.__HexColor = hc
