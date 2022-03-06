class Driver():
    #isi atribut driver
    licenseID = 0
    activeUntil = 0
    vehicleType = ""
    
    #init
    def __init__(self, f, p, n):
        self.licenseID = f
        self.activeUntil = p
        self.vehicleType = n
    
    #setter getter
    def setLicenseID(self, i):
        self.licenseID = i
    
    def getLicenseID(self):
        return self.licenseID
    
    def setActive(self, p):
        self.activeUntil = p
    
    def getActive(self):
        return self._ctiveUntil
    
    def setVehicle(self, i):
        self.vehicleType = i
    
    def getVehicle(self):
        return self.vehicleType