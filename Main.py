#import class
from Driver import Driver
from Job import Job
from Person import Person

from Vehicle import Vehicle
from Ship import Ship
from Airplane import Airplane

#class person
print('============== Driver License Data ==============')

#isi atribut job dan driver
job1 = Job(1234, "Microsoft", "Manager")
driver1 = Driver(4567, 2023, "Car")

#input class job dan driver ke class person
p1 = Person(8940, True, "Asep", job1, driver1)

job2 = Job(7839, "Apple", "CEO")
driver2 = Driver(9842, 2018, "Motorcycle")
p2 = Person(7389, True, "Bobon", job2, driver2)

job3 = Job(8475, "Facebook", "Accounting Manager")
driver3 = Driver(8992, 2022, "Truck")
p3 = Person(9025, False, "Ceceu", job3, driver3)

job4 = Job(2309, "Amazon", "COO")
driver4 = Driver(1293, 2006, "Car")
p4 = Person(9834, False, "Dina", job4, driver4)

job5 = Job(7823, "Google", "Senior Programmer")
driver5 = Driver(7834, 2001, "Car")
p5 = Person(7345, True, "Edi", job5, driver5)

#jalankan prosedur printd dari class person
p1.sleep()
p2.sleep()
p3.sleep()
p4.sleep()
p5.sleep()

#class vehicle
print('================== Vehicle Data =================')

#isi atribut vehicle
vehicle1=Vehicle("Diesel", "Kapal1", 100, 5, "Cruise")

#masukkan isi class vehicle antara ke ship aatau airplane sesuai data yang mau diinput
v1 = Ship(vehicle1, "Indonesia")

vehicle2=Vehicle("Diesel", "Kapal2", 5, 1, "Yacht")
v2 = Ship(vehicle2, "USA")

vehicle3=Vehicle("Electric", "Pesawat1", 2, 0, "Fighter Jet")
v3 = Airplane(vehicle3, 4)

vehicle4=Vehicle("Diesel", "Pesawat2", 50, 1, "737")
v4 = Airplane(vehicle4, 10)

vehicle5=Vehicle("Unknown", "Pesawat3", 100000, 0, "Death Star")
v5 = Airplane(vehicle5, 10000)

#prosedur print data vehicle
v1.printData()
v2.printData()
v3.printData()
v4.printData()
v5.printData()

#Saya Irfan Mochamad Esa 2005568 mengerjakan LATIHAN4 dalam mata kuliah Desain dan Pemrograman Berbasis Objek untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin