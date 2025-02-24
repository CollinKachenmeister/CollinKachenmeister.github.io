"""
Grazioso Enhancement 1 - Software Design and Engineering

This version of the program is written in Python and fixes minor input validation

"""

from Dog import Dog
from Monkey import Monkey
import random
import timeit

# Create new lists for dogs and monkeys
dogList = []
monkeyList = []

# Adds dogs to the list for testing
def initializeDogList():
    #dog1 = Dog("Spot", "German Shepherd", "male", "1", "25.6", "05-12-2019", "United States", "intake", False, "United States", "Dog")
    #dog2 = Dog("Rex", "Great Dane", "male", "3", "35.2", "02-03-2020", "United States", "Phase I", False, "United States", "Dog")
    #dog3 = Dog("Bella", "Chihuahua", "female", "4", "25.6", "12-12-2019", "Canada", "in service", True, "Canada", "Dog")

    #dogList.append(dog1)
    #dogList.append(dog2)
    #dogList.append(dog3)

    breeds = ["German Shepherd", "Great Dane", "Chihuahua", "Poodle", "Rottweiler", "Bulldog"]

    for i in range(50):
        name = f"Dog{i+1}"
        i = Dog(
            name = name,
            breed = breeds[random.randint(0,5)],
            gender = "male" if (str(random.randint(1,2)) == "1") else "female",
            age = str(random.randint(1,10)),
            weight = str(random.randint(20,40)) + ".0",
            acquisitionDate = "05-12-2019",
            acquisitionCountry= "United States",
            trainingStatus= "intake",
            reserved = False,
            inServiceCountry="United States",
            animalType="Dog"   
        )
        dogList.append(i)
# Adds monkeys to the list for testing
def initializeMonkeyList():
    monkey1 = Monkey("Fred", "Capuchin", "10.2", "30.4", "25.6", "male", "5", "28.7", "05-12-2019", "United States", "intake", False, "United States", "Monkey")
    monkey2 = Monkey("Winston", "Guenon", "15.6", "35.9", "35.2", "male", "4", "30.7", "02-03-2020", "United States", "Phase I", True, "United States", "Monkey");
    monkey3 = Monkey("Bananas", "Macaque", "20.8", "40.8", "25.6", "female", "3","24.6", "12-12-2019", "Canada", "in service", False, "Canada", "Monkey")

    monkeyList.append(monkey1)
    monkeyList.append(monkey2)
    monkeyList.append(monkey3)

# Prompts the user to input information for new dog and adds the dog to the list
def intakeNewDog():
    name = input("What is the dog's name?\n")

    # Checks for duplicate names in the dog list
    for dog in dogList:
        if dog.getName().lower() == name.lower():
            print("\n\nThis dog is already in our system\n\n")
            return
        
    breed = input("What is the dog's breed?\n")
    gender = input("What is the dog's gender?\n")
    age = input("What is the dog's age?\n")
    weight = input("What is the dog's weight?\n")
    acquisitionDate = input("What is the dog's acquisition date?\n")
    acquisitionCountry = input("What is the dog's acquisition country?\n")
    trainingStatus = input("What is the dog's training status?\n")

    # Input validation for reserve status
    quit = False
    while not quit:
        reservedStatus = input("Is the dog reserved? (true or false)\n")

        if reservedStatus.strip().lower() == "true":
            reserved = True
            quit = True
        elif reservedStatus.strip().lower() == "false":
            reserved = False
            quit = True
        else:
            print("Invalid response please try again.\n")
    
    inServiceCountry = input("What is the dog's service country?\n")

    # Adds the new dog to the dog list
    newDog = Dog(name, breed, gender, age, weight, acquisitionDate, acquisitionCountry, trainingStatus, reserved, inServiceCountry, "Dog")
    dogList.append(newDog)
    print(name + " was added to the list")

# Prompts the user to input information for the new monkey and adds the monkey to the list
def intakeNewMonkey():
    name = input("What is the monkey's name?\n")

    # Checks for duplicate names in the monkey list
    for monkey in monkeyList:
        if monkey.getName().lower() == name.lower():
            print("\n\nThis monkey is already in our system\n\n")
            return
    
    # Eligible monkey species
    eligibleSpecies = ["capuchin", "guenon", "macaque", "marmoset", "squirrel monkey", "tamarin"]

    # Input validation for eligible monkey species
    species = input("What is the monkey's species?\n").lower().strip()
    if species not in eligibleSpecies:
        print("\n\nThis species of monkey is not eligible for training\n\n")
        return
    
    tailLength = input("What is the monkey's tail length?\n")
    height = input("What is the monkey's height?\n")
    bodyLength = input("What is the monkey's body length?\n")
    gender = input("What is the monkey's gender?\n")
    age = input("What is the monkey's age?\n")
    weight = input("What is the monkey's weight?\n")
    acquisitionDate = input("What is the monkey's acquisition date?\n")
    acquisitionCountry = input("What is the monkey's acquisition country?\n")
    trainingStatus = input("What is the monkey's training status?\n")

    # Input validation for reserve status
    quit = False
    while not quit:
        reservedStatus = input("Is the monkey reserved? (true or false)\n")

        if reservedStatus.strip().lower() == "true":
            reserved = True
            quit = True
        elif reservedStatus.strip().lower() == "false":
            reserved = False
            quit = True
        else:
            print("Invalid response please try again.\n")
    
    inServiceCountry = input("What is the monkey's service country?\n")

    # Adds the new monkey to the monkey list
    newMonkey = Monkey(name, species, tailLength, height, bodyLength, gender, age, weight, acquisitionDate, acquisitionCountry,
                    trainingStatus, reserved, inServiceCountry, "Monkey")
    monkeyList.append(newMonkey)
    print(name + " was added to the list")

# User inputs animal type and reserves the first animal found in the list of that type
def reserveAnimal():
    animalType = input("Enter the animal type you wish to search for (dog or monkey):\n").strip().lower()

    # Input validation for animal type
    while animalType not in ["dog", "monkey"]:
        print("Invalid animal type. Please enter 'dog' or 'monkey':\n")
        animalType = input().strip().lower()
    
    inServiceCountry = input("Enter the animal's in-service country\n").strip()
    # Boolean for tracking if animal is reserved successfully 
    found = False

    # Iterates through the dog list and checks for user input in-service country and not reserved
    if animalType == "dog":
        for d in dogList:
            if d.getInServiceCountry().lower() == inServiceCountry.lower() and not d.getReserved():
                d.setReserved(True)
                print(d.getName() + " was reserved.")
                found = True
                break
        if not found:
            print(f"No {animalType} is available in {inServiceCountry}")

    # Iterates through the monkey list and checks for user input in-service country and not reserved
    else:
        for m in monkeyList:
            if m.getInServiceCountry().lower() == inServiceCountry.lower() and not m.getReserved():
                m.setReserved(True)
                print(m.getName() + " was reserved.")
                found = True
                break
        if not found:
            print(f"No {animalType} is available in {inServiceCountry}")

# Prints a list of all dogs, all monkeys, or all animals in service and not reserved
def printAnimals(listType):

    # Prints a list of all dogs
    if listType == "Dog":
        print("\nList of dogs:\n")
        for d in dogList:
            print(f"Name: {d.getName()}, status: {d.getTrainingStatus()}, acquisition country: {d.getAcquisitionCountry()}, reserved: {d.getReserved()}")
        return

    # Prints a list of all monkeys
    if listType == "Monkey":
        print("\nList of monkeys:\n")
        for m in monkeyList:
            print(f"Name: {m.getName()}, status: {m.getTrainingStatus()}, acquisition country: {m.getAcquisitionCountry()}, reserved: {m.getReserved()}")
        return
    
    # Prints a list of all animals in service and not reserved
    found = False
    if listType == "Available":
        for d in dogList:
            if d.getTrainingStatus().lower() == "in service" and not d.getReserved():
                print(f"Animal type: {d.getAnimalType()}, name: {d.getName()}, status: {d.getTrainingStatus()}, acquisition country: {d.getAcquisitionCountry()}, reserved: {d.getReserved()}")
                found = True

        for m in monkeyList:
            if m.getTrainingStatus().lower() == "in service" and not m.getReserved():
                print(f"Animal type: {m.getAnimalType()}, name: {m.getName()}, status: {m.getTrainingStatus()}, acquisition country: {m.getAcquisitionCountry()}, reserved: {m.getReserved()}")                 
                found = True
        
        if not found:
            print("No animals are in service and not reserved\n")

# Test time to search for random dog
# Uncomment the following lines of code and change initializeDogList to 10000 to test
def testDogList():
    name = "Dog" + str(random.randint(0,10000))
    for d in dogList:
        if name == d.getName():
            return d.getName()
    else:
        return None
            


# Prints the menu options
def displayMenu():
    print("\n\n\t\t\t\tRescue Animal System Menu")
    print("[1] Intake a new dog")
    print("[2] Intake a new monkey")
    print("[3] Reserve an animal")
    print("[4] Print a list of all dogs")
    print("[5] Print a list of all monkeys")
    print("[6] Print a list of all animals that are not reserved")
    # Uncomment the following line to test lookup time
    #print("[7] Test time to search for random dog")
    print("[q] Quit application\n")
    print("Enter a menu selection:")

# Main method initializes the dog and monkey list, displays menu options, and
# loops until the user enters 'q' to quit the program
def main():

    # Initialize both lists
    initializeDogList()
    initializeMonkeyList()

    # Loop menu until user quits
    quit = False
    while not quit:
        displayMenu()
        menuSelection = input().strip().lower()

        if menuSelection == "1":
            intakeNewDog()

        elif menuSelection == "2":
            intakeNewMonkey()

        elif menuSelection == "3":
            reserveAnimal()

        elif menuSelection == "4":
            printAnimals("Dog")
        
        elif menuSelection == "5":
            printAnimals("Monkey")
        
        elif menuSelection == "6":
            printAnimals("Available")

        # Uncomment to test lookup time
        #elif menuSelection == "7":
        #    time = timeit.timeit(testDogList, number=1000)
        #    print(f"Lookup time is {time:.8f} seconds")

        elif menuSelection == "q":
            print("The application has been quit.")
            quit = True
        
        else:
            print("Invalid menu selection")

main()


