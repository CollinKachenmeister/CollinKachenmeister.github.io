"""
Grazioso Enhancement 2 - Algorithms and Data Structure

This version of the program is written in Python, utilizes dictionaries instead of lists,
adds multiple dogs and monkeys for testing, includes new functions, and tests lookup time

"""

from Dog import Dog
from Monkey import Monkey
import random
import timeit

# Create new dictionaries for dogs and monkeys
dogList = {}
monkeyList = {}

# Adds dogs to the list for testing. Number of dogs can be changed.
def initializeDogList():

    breeds = ["German Shepherd", "Great Dane", "Chihuahua", "Poodle", "Rottweiler", "Bulldog"]

    for i in range(50):
        name = f"Dog{i+1}"
        dogList[name] = Dog(
            name = name,
            breed = breeds[random.randint(0,5)],
            gender = "male" if (str(random.randint(1,2)) == "1") else "female",
            age = str(random.randint(1,10)),
            weight = str(random.randint(20,40)) + ".0",
            acquisitionDate = "05-12-2019",
            acquisitionCountry= "United States",
            trainingStatus= "intake" if str(random.randint(1,3)) == "1" else "in service",
            reserved = False if str(random.randint(1,2)) == "1" else True,
            inServiceCountry="United States",
            animalType="Dog"
        )

# Adds 50 monkeys to the list for testing. Number of monkeys can be changed.
def initializeMonkeyList():

    eligibleSpecies = ["capuchin", "guenon", "macaque", "marmoset", "squirrel monkey", "tamarin"]

    for i in range(50):
        name = f"Monkey{i+1}"
        monkeyList[name] = Monkey(
            name = name,
            species = eligibleSpecies[random.randint(0,5)],
            tailLength = str(random.randint(1,100)),
            height = str(random.randint(1,100)),
            bodyLength = str(random.randint(1,100)),
            gender = "male" if (str(random.randint(1,2)) == "1") else "female",
            age = str(random.randint(1,10)),
            weight = str(random.randint(20,40)) + ".0",
            acquisitionDate = "05-12-2019",
            acquisitionCountry= "United States",
            trainingStatus= "intake" if str(random.randint(1,3)) == "1" else "in service",
            reserved = False if str(random.randint(1,2)) == "1" else True,
            inServiceCountry="United States",
            animalType="Monkey"
        )

# Prompts the user to input information for new dog and adds the dog to the list
def intakeNewDog():
    name = input("What is the dog's name?\n")

    if name in dogList:
        print("\nThis dog is already in our system\n")
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
    dogList[name] = Dog(name, breed, gender, age, weight, acquisitionDate, acquisitionCountry, trainingStatus, reserved, inServiceCountry, "Dog")
    print(name + " was added to the list")

# Prompts the user to input information for the new monkey and adds the monkey to the list
def intakeNewMonkey():
    name = input("What is the monkey's name?\n")

    # Checks for duplicate names in the monkey list
    if name in monkeyList:
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
    monkeyList[name] = Monkey(name, species, tailLength, height, bodyLength, gender, age, weight, acquisitionDate, acquisitionCountry,
                    trainingStatus, reserved, inServiceCountry, "Monkey")
    print(name + " was added to the list")

# User inputs animal type and name and reserves the animal if it is not already reserved
def reserveAnimal():
    animalType = input("Enter the animal type you wish to search for (dog or monkey):\n").strip().lower()

    # Input validation for animal type
    while animalType not in ["dog", "monkey"]:
        print("Invalid animal type. Please enter 'dog' or 'monkey':\n")
        animalType = input().strip().lower()
    
    name = input("What is the animal's name?: ")

    # Iterates through the dog list and checks for user input in-service country and not reserved
    if animalType == "dog":
        if name in dogList:
            if not dogList[name].getReserved():
                dogList[name].setReserved(True)
                print(f"{name} was reserved.")
            else:
                print(f"{name} is already reserved.")

    # Iterates through the monkey list and checks for user input in-service country and not reserved
    elif animalType == "monkey":
        if name in monkeyList:
            if not monkeyList[name].getReserved():
                monkeyList[name].setReserved(True)
                print(f"{name} was reserved.")
            else:
                print(f"{name} is already reserved.")
    
    else:
        print(f"No {animalType} found with the name {name}")

# Prints a list of all dogs, all monkeys, or all animals in service and not reserved
def printAnimals(listType):

    # Prints a list of all dogs
    if listType == "Dog":
        print("\nList of dogs:\n")
        for d in dogList.values():
            print(vars(d))
        return

    # Prints a list of all monkeys
    if listType == "Monkey":
        print("\nList of monkeys:\n")
        for m in monkeyList.values():
            print(vars(m))
        return
    
    # Prints a list of all animals in service and not reserved
    found = False
    if listType == "Available":
        for d in dogList.values():
            if d.getTrainingStatus().lower() == "in service" and not d.getReserved():
                print(f"Animal type: {d.getAnimalType()}, name: {d.getName()}, status: {d.getTrainingStatus()}, acquisition country: {d.getAcquisitionCountry()}, reserved: {d.getReserved()}")
                found = True

        for m in monkeyList.values():
            if m.getTrainingStatus().lower() == "in service" and not m.getReserved():
                print(f"Animal type: {m.getAnimalType()}, name: {m.getName()}, status: {m.getTrainingStatus()}, acquisition country: {m.getAcquisitionCountry()}, reserved: {m.getReserved()}")                 
                found = True
        
        if not found:
            print("No animals are in service and not reserved\n")

# Searches the dog or monkey list for the name of the animal.
def searchByName():
    animalType = input("What type of animal do you want to search for? (Dog or Monkey): ").strip().lower()
    if animalType == "dog":
        name = input("What is the dog's name?: ").strip()
        if name in dogList:
            print(vars(dogList[name]))
        else:
            print(f"{name} not found.")
    elif animalType == "monkey":
        name = input("What is the monkey's name?: ").strip()
        if name in monkeyList:
            print(vars(monkeyList[name]))
        else:
            print(f"{name} not found.")
    else:
        print(f"{animalType} is not an acceptable type of animal. Please enter dog or monkey")

# Searches for the dog breed
def searchByBreed():
    breeds = ["german shepherd", "great dane", "chihuahua", "poodle", "rottweiler", "bulldog"]
    breed = input("Enter dog breed: ").strip().lower()
    if breed not in breeds:
        print(f"{breed} not found")
    else:
        for d in dogList.values():
            if d.getBreed().lower() == breed:
                print(vars(d))

# Searches for the monkey species
def searchBySpecies():
    eligibleSpecies = ["capuchin", "guenon", "macaque", "marmoset", "squirrel monkey", "tamarin"]
    species = input("Enter monkey species: ").strip().lower()
    if species not in eligibleSpecies:
        print(f"{species} not found")
    else:
        for m in monkeyList.values():
            if m.getSpecies().lower() == species:
                print(vars(m))
    

# Test time to search for random dog
# Please uncomment the following code and change the initializeDogList to 10000
#def testDogList():
#    name = "Dog" + str(random.randint(0,10000))
#    return dogList.get(name, None)
    
# Prints the menu options
def displayMenu():
    print("\n\n\t\t\t\tRescue Animal System Menu")
    print("[1] Intake a new dog")
    print("[2] Intake a new monkey")
    print("[3] Reserve an animal by name")
    print("[4] Print a list of all dogs")
    print("[5] Print a list of all monkeys")
    print("[6] Print a list of all animals that are not reserved")
    print("[7] Search for animal by name")
    print("[8] Search for dog by breed")
    print("[9] Search for monkey by species")
    # Uncomment the following line to test search time
    print("[11] Test time to search dictionary")
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

        elif menuSelection == "7":
            searchByName()
        
        elif menuSelection == "8":
            searchByBreed()

        elif menuSelection == "9":
            searchBySpecies()

        # Uncomment the following lines of code to test search time
        #elif menuSelection == "11":
        #    time = timeit.timeit(testDogList, number = 1000)
        #    print(f"Lookup time is {time:.8f} seconds")

        elif menuSelection == "q":
            print("The application has been quit.")
            quit = True

        else:
            print("Invalid menu selection")

main()


