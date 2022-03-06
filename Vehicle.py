#vehicle menggunakan prinsip inheritance dimana vehicle diinherit oleh ship dan airplane
import random #import library random untuk menentukan apakah kendaraan sedang jalan atau tidak

class Vehicle():
    #atribut vehicle
    __name = ""
    __fuelType = ""
    __maxPassengers = 0
    __age = 0
    __type = ""
    
    #init
    def __init__(self, f, n, p, a, t):
        self.__fuelType = f
        self.__name = n
        self.__maxPassengers = p
        self.__age = a
        self.__type = t
    
    #setter getter
    def setFuel(self, i):
        self.__fuelType = i
    
    def getFuel(self):
        return self.__fuelType
    
    def setPassengers(self, p):
        self.__maxPassengers = p
    
    def getPassengers(self):
        return self.__maxPassengers
    
    def setName(self, i):
        self.__name = i
    
    def getName(self):
        return self.__name
    
    def setAge(self, a):
        self.__age = a
    
    def getAge(self):
        return self.__age
    
    def setType(self, i):
        self.__type = i
    
    def getType(self):
        return self.__type
    
    #prosedur print vehicle
    def move(self):
        print((self.getName()))
        print("Fuel           :", self.getFuel())
        print("Max Passengers :", self.getPassengers())
        print("Age            :", self.getAge())
        print("Type           :", self.getType())
        
        #random menentukan 0 atau 1
        state = random.getrandbits(1)
        if (state>0):
            print("State          : is operating")
        else :
            print("State          : is idle")