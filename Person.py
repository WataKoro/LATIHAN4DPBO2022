#class person menggunakan prinsip multiple inheritance
#dimana person menginherit class job dan driver
from Job import Job
from Driver import Driver
import random #library random untuk menentukan apakah orangnya sedang tidur atau tidak

class Person(Job, Driver):
    #atribut person
    __id = 0
    __gender = False
    __name = ""
    
    #init
    def __init__(self, f, p, n, job, driver):
        self.__Job = job
        self.__driver = driver
        self.__id = f
        self.__name = n
        self.__gender = p
    
    #setter getter
    def setJob(self, i):
        self.__Job = i
    
    def getJob(self):
        return self.__Job

    def setDriver(self, i):
        self.__driver = i
    
    def getDriver(self):
        return self.__driver
        
    def setID(self, i):
        self.__id = i
    
    def getID(self):
        return self.__id
    
    def setGender(self, p):
        self.__gender = p
    
    def getGender(self):
        return self.__gender
    
    def setName(self, i):
        self.__name = i
    
    def getName(self):
        return self.__name
    
    #prosedur print isi
    def sleep(self):
        print((self.__name), "whose job is", (self.__Job.position), "for", (self.__Job.company))
        
        #gender berupa boolean dimana true = male dan false = female
        if(self.__gender == True):
            print ("is a male", "NIK :", (self.__id), "NIP", (self.__Job.workID))
        else:
            print ("is a female", "NIK :", (self.__id), "NIP", (self.__Job.workID))
            
        #syarat sim hanya valid jika tahun berlaku belum lewat
        if (self.__driver.activeUntil >= 2022):
            print("-> has a driver license for a", (self.__driver.vehicleType), "ID :", self.__driver.licenseID)
        else :
            print("-> doesn't have a driver license")
        
        state = random.getrandbits(1) #cari nilai random antara 0 dan 1 untuk menentukan apakah lagi tidur atau tidak
        if (state>0):
            print("-> is sleeping")
        else :
            print("-> is not sleeping")
        print('=================================================')