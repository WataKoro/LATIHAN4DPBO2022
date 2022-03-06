from Vehicle import Vehicle #import class vehicle

class Ship(Vehicle):
    #isi atribut ship
    __countryOfManufacture = ""
    
    #init
    def __init__(self, v, c):
        self.__Vehicle = v
        self.__countryOfManufacture = c
    
    #setter getter
    def setVehicle(self, i):
        self.__Vehicle = i
    
    def getVehicle(self):
        return self.__Vehicle

    def setCountry(self, i):
        self.__countryOfManufacture = i
    
    def getCountry(self):
        return self.__countryOfManufacture
    
    #print asal negara dan memanggil prosedur print isi vehicle
    def printData(self):
        self.__Vehicle.move()
        print(self.__countryOfManufacture)
        print('=================================================')