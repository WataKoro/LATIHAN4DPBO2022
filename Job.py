class Job():
    #atribut job
    workID = 0
    company = ""
    position = ""
    
    #init
    def __init__(self, f, p, n):
        self.workID = f
        self.company = p
        self.position = n
    
    #setter getter
    def setWorkID(self, i):
        self.workID = i
    
    def getWorkID(self):
        return self.workID
    
    def setCompany(self, p):
        self.company = p
    
    def getCompany(self):
        return self.company
    
    def setPosition(self, i):
        self.position = i
    
    def getPosition(self):
        return self.position