# Parent class containing attributes applicable to both Dog and Monkey
class RescueAnimal:

    # Attributes
    def __init__(self):
        self.name = ""
        self.animalType = ""
        self.gender = ""
        self.age = ""
        self.weight = ""
        self.acquisitionDate = ""
        self.acquisitionCountry = ""
        self.trainingStatus = ""
        self.reserved = False
        self.inServiceCountry = ""
    
    # Getters
    def getName(self):
        return self.name
    
    def getAnimalType(self):
        return self.animalType
    
    def getGender(self):
        return self.gender
    
    def getAge(self):
        return self.age
    
    def getWeight(self):
        return self.weight
    
    def getAcquisitionDate(self):
        return self.acquisitionDate
    
    def getAcquisitionCountry(self):
        return self.acquisitionCountry
    
    def getTrainingStatus(self):
        return self.trainingStatus
    
    def getReserved(self):
        return self.reserved
    
    def getInServiceCountry(self):
        return self.inServiceCountry
    
    # Setters
    def setName(self, name):
        self.name = name
    
    def setAnimalType(self, animalType):
        self.animalType = animalType
    
    def setGender(self, gender):
        self.gender = gender
    
    def setAge(self, age):
        self.age = age
    
    def setWeight(self, weight):
        self.weight = weight
    
    def setAcquisitionDate(self, acquisitionDate):
        self.acquisitionDate = acquisitionDate
    
    def setAcquisitionCountry(self, acquisitionCountry):
        self.acquisitionCountry = acquisitionCountry
    
    def setTrainingStatus(self, trainingStatus):
        self.trainingStatus = trainingStatus
    
    def setReserved(self, reserved):
        self.reserved = reserved
    
    def setInServiceCountry(self, inServiceCountry):
        self.inServiceCountry = inServiceCountry
    
