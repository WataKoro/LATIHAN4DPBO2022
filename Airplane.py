from Vehicle import Vehicle #import class vehicle

class Airplane(Vehicle):
    #isi atribut airplane
    __wingsLength = 0
    
    #init
    def __init__(self, v, w):
        self.__Vehicle = v
        self.__wingsLength = w
    
    #setter getter
    def setVehicle(self, i):
        self.__Vehicle = i
    
    def getVehicle(self):
        return self.__Vehicle
    
    def setWings(self, i):
        self.__wingsLength = i
    
    def getWings(self):
        return self.__wingsLength
    
    #print panjang sayap pesawat dan memanggil prosedur print isi vehicle
    def printData(self):
        self.__Vehicle.move()
        print(self.__wingsLength, "Meter(s)")
        print('=================================================')