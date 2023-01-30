class Client():

    def __init__(self, name, dni, address, phone):
        self.name = name
        self.dni = dni
        self.address = address
        self.phone = phone
    
    def getName(self):
        return self.name
    
    def getDni(self):
        return self.dni
    
    def getAddress(self):
        return self.address
    
    def getPhone(self):
        return self.phone
    
    def setName(self, name):
        self.name = name
    
    def setDni(self, dni):
        self.dni = dni
    
    def setAddress(self, address):
        self.address = address
    
    def setPhone(self, phone):
        self.phone = phone