class Product:

    def __init__(self, name, data: dict):
        self.name = name
        self.data = data

    def getName(self):
        return self.name
    
    def getData(self, key):
        return self.data.get(key)
    
    def setName(self, name):
        self.name = name
    
    def setData(self, data):
        self.data = data