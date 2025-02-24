from RescueAnimal import RescueAnimal

# Monkey class extends RescueAnimal
class Monkey(RescueAnimal):
    
    # Default constructor
    def __init__(self, name, species, tailLength, height, 
               bodyLength, gender, age, weight, acquisitionDate, 
               acquisitionCountry, trainingStatus, reserved, 
               inServiceCountry, animalType):
        
        # Superclass constructor
        super().__init__()
        self.tailLength = tailLength
        self.height = height
        self.bodyLength = bodyLength
        self.species = species

        self.setName(name)
        self.setGender(gender)
        self.setAge(age)
        self.setWeight(weight)
        self.setAcquisitionDate(acquisitionDate)
        self.setAcquisitionCountry(acquisitionCountry)
        self.setTrainingStatus(trainingStatus)
        self.setReserved(reserved)
        self.setInServiceCountry(inServiceCountry)
        self.setAnimalType(animalType)
    
    #Getters
    def getTailLength(self):
        return self.tailLength
    
    def getHeight(self):
        return self.height
    
    def getBodyLength(self):
        return self.bodyLength
    
    def getSpecies(self):
        return self.species
    
    #Setters
    def setTailLength(self, tailLength):
        self.tailLength = tailLength
    
    def setHeight(self, height):
        self.height = height
    
    def setBodyLength(self, bodyLength):
        self.bodyLength = bodyLength
    
    def setSpecies(self, species):
        self.species = species

