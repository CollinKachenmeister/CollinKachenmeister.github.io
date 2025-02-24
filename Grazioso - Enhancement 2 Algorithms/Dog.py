from RescueAnimal import RescueAnimal

# Dog class extends RescueAnimal
class Dog(RescueAnimal):

    # Default constructor
    def __init__(self, name, breed, gender, age, 
               weight, acquisitionDate, acquisitionCountry, 
               trainingStatus, reserved, inServiceCountry, animalType):

        # Superclass constructor 
        super().__init__()
        self.breed = breed

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
    def getBreed(self):
        return self.breed
    
    #Setters
    def setBreed(self, dogBreed):
        self.breed = dogBreed
        