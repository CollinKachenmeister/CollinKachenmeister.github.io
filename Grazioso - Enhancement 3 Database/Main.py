"""
Grazioso Enhancement 3 - Databases

This version of the program is written in Python and utilizes SQLite to create a database for persistent storage

Includes function to remove animal from database

"""

from Dog import Dog
from Monkey import Monkey
import random
import sqlite3

# Connect to sqlite
conn = sqlite3.connect('animals.db')

# Create cursor object
cursor = conn.cursor()

# Create tables if they do not exist
def createTables():
    cursor.execute('''CREATE TABLE IF NOT EXISTS dogs (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT UNIQUE,
                   breed TEXT,
                   gender TEXT,
                   age TEXT,
                   weight TEXT,
                   acquisitionDate TEXT,
                   acquisitionCountry TEXT,
                   trainingStatus TEXT,
                   reserved BOOLEAN,
                   inServiceCountry TEXT,
                   animalType TEXT)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS monkeys (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT UNIQUE,
                   species TEXT,
                   tailLength TEXT,
                   height TEXT,
                   bodyLength TEXT,
                   gender TEXT,
                   age TEXT,
                   weight TEXT,
                   acquisitionDate TEXT,
                   acquisitionCountry TEXT,
                   trainingStatus TEXT,
                   reserved BOOLEAN,
                   inServiceCountry TEXT,
                   animalType TEXT)''')
    
    # Commit changes to database
    conn.commit()

    # Close the connection
    conn.close()

# Add dogs and monkeys to respective tables for testing
def populateTestData():
    # Connect to sqlite
    conn = sqlite3.connect('animals.db')

    # Create cursor object
    cursor = conn.cursor()

    # Possible choices for dog breeds
    breeds = ["German Shepherd", "Great Dane", "Chihuahua", "Poodle", "Rottweiler", "Bulldog"]

    # Eligible monkey species
    eligibleSpecies = ["capuchin", "guenon", "macaque", "marmoset", "squirrel monkey", "tamarin"]

    # Query to INSERT dog records
    for i in range(50):
        name = f"Dog{i+1}"
        cursor.execute('''INSERT or IGNORE INTO dogs (name, breed, gender, age, weight, acquisitionDate, acquisitionCountry, trainingStatus, reserved, inServiceCountry, animalType) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
        (name,
         random.choice(breeds),
         random.choice(['male', 'female']),
         str(random.randint(1,10)),
         str(random.randint(20,40)) + ".0",
         "05-12-2019",
         "United States",
         random.choice(['intake', 'in service']),
         random.choice([True, False]),
         "United States",
         "Dog"
         )) 
    
    # Query to INSERT monkey records
    for i in range(50):
        name = f"Monkey{i+1}"
        cursor.execute('''INSERT or IGNORE INTO monkeys (name, species, tailLength, height, bodyLength, gender, age, weight, acquisitionDate, acquisitionCountry, trainingStatus, reserved, inServiceCountry, animalType) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
        (name,
         random.choice(eligibleSpecies),
         str(random.randint(1,100)),
         str(random.randint(1,100)),
         str(random.randint(1,100)),
         random.choice(['male', 'female']),
         str(random.randint(1,10)),
         str(random.randint(20,40)) + ".0",
         "05-12-2019",
         "United States",
         random.choice(['intake', 'in service']),
         random.choice([True, False]),
         "United States",
         "Monkey"
         ))
        
    # Commit changes to database
    conn.commit()

    # Close the connection
    conn.close()

# Adds a dog to the dog table if animal name does not already exist
def intakeNewDog():
    # Connect to sqlite and create cursor object
    conn = sqlite3.connect('animals.db')
    cursor = conn.cursor()

    name = input("What is the dog's name?\n")
    
    # Query to check the table if name already exists
    cursor.execute("SELECT name FROM dogs WHERE name = ?", (name,))
    if cursor.fetchone():
        print("\nThis dog is already in our system\n")
        conn.close()
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

    # Query to insert the record into the database
    cursor.execute('''INSERT INTO dogs(name, breed, gender, age, weight, acquisitionDate, acquisitionCountry, trainingStatus, reserved, inServiceCountry, animalType) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
                   (name, breed, gender, age, weight, acquisitionDate, acquisitionCountry, trainingStatus, reserved, inServiceCountry, 'Dog'))
     # Commit changes to database and close connection
    conn.commit()
    conn.close()
    
    # Display message that dog was added successfully 
    print(name + " was added to the list")

# Prompts the user to input information for the new monkey and adds the monkey to the list
def intakeNewMonkey():
    # Connect to sqlite and create cursor object
    conn = sqlite3.connect('animals.db')
    cursor = conn.cursor()

    name = input("What is the monkey's name?\n")
    
    # Query to check the table if name already exists
    cursor.execute("SELECT name FROM monkeys WHERE name = ?", (name,))
    if cursor.fetchone():
        print("\nThis monkey is already in our system\n")
        conn.close()
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

    # Query to insert the record into the database
    cursor.execute('''INSERT INTO monkeys(name, species, tailLength, height, bodyLength, gender, age, weight, acquisitionDate, acquisitionCountry, trainingStatus, reserved, inServiceCountry, animalType) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
                   (name, species, tailLength, height, bodyLength, gender, age, weight, acquisitionDate, acquisitionCountry, trainingStatus, reserved, inServiceCountry, 'Monkey'))
    
     # Commit changes to database and close connection
    conn.commit()
    conn.close()

    # Display message that dog was added successfully
    print(name + " was added to the list")

# User inputs animal type and name and reserves the animal if it is not already reserved
def reserveAnimal():
    animalType = input("Enter the animal type you wish to search for (dog or monkey):\n").strip().lower()

    # Input validation for animal type
    while animalType not in ["dog", "monkey"]:
        print("Invalid animal type. Please enter 'dog' or 'monkey':\n")
        animalType = input().strip().lower()
    
    name = input("What is the animal's name?: ")

    # Connect to sqlite and create cursor object
    conn = sqlite3.connect('animals.db')
    cursor = conn.cursor()

    # Check dog or monkey table for animal type and name
    if animalType == "dog":
        cursor.execute('''UPDATE dogs SET reserved = 1 WHERE name = ?''', (name,))
    elif animalType == "monkey":
        cursor.execute('''UPDATE monkeys SET reserved = 1 WHERE name = ?''', (name,))
    else:
        print(f"No {animalType} found with the name {name}")
        return
    
    # Commit changes to database and close connection
    conn.commit()
    conn.close()

    # Display message that dog was added successfully
    print(name + " was reserved")

# Print a list of all dogs, monkeys, or animals that are not reserved
def printAnimals(type):

    # Connect to sqlite and create cursor object
    conn = sqlite3.connect('animals.db')
    cursor = conn.cursor()

    if type == "Dog":
        cursor.execute('''SELECT * FROM dogs''')
        dogs = cursor.fetchall()
        print("\nList of dogs:\n")
        for dog in dogs:
            print(dog)

    elif type == "Monkey":
        cursor.execute('''SELECT * FROM monkeys''')
        monkeys = cursor.fetchall()
        print("\nList of monkeys:\n")
        for monkey in monkeys:
            print(monkey)
    
    elif type == "Available":
        cursor.execute('''SELECT * FROM dogs WHERE reserved = 0''')
        availableDogs = cursor.fetchall()
        cursor.execute('''SELECT * FROM monkeys WHERE reserved = 0''')
        availableMonkeys = cursor.fetchall()

        print("\nList of all unreserved dogs:\n")
        for dog in availableDogs:
            print(dog)

        print("\nList of all unreserved monkeys:\n")
        for monkey in availableMonkeys:
            print(monkey)

    # Commit changes to database and close connection
    conn.commit()
    conn.close()

# Searches the dog or monkey list for the name of the animal.
def searchByName():
    # Connect to sqlite and create cursor object
    conn = sqlite3.connect('animals.db')
    cursor = conn.cursor()

    animalType = input("What type of animal do you want to search for? (Dog or Monkey): ").strip().lower()

    # Input validation for animal type
    while animalType not in ["dog", "monkey"]:
        print("Invalid animal type. Please enter 'dog' or 'monkey':\n")
        animalType = input().strip().lower()
    
    if animalType == "dog":
        name = input("What is the dog's name?: ").strip()
        cursor.execute('''SELECT * FROM dogs WHERE name = ?''', (name,))
        dog = cursor.fetchone()
        if dog:
            print(dog)
        else:
            print(f"{name} not found.")

    elif animalType == "monkey":
        name = input("What is the monkey's name?: ").strip()
        cursor.execute('''SELECT * FROM monkeys WHERE name = ?''', (name,))
        monkey = cursor.fetchone()
        if monkey:
            print(monkey)
        else:
            print(f"{name} not found.")

    # Commit changes to database and close connection
    conn.commit()
    conn.close()

# Searches for the dog breed
def searchByBreed():
    # Connect to sqlite and create cursor object
    conn = sqlite3.connect('animals.db')
    cursor = conn.cursor()

    breeds = ["german shepherd", "great dane", "chihuahua", "poodle", "rottweiler", "bulldog"]
    breed = input("Enter dog breed: ").strip().lower()
    if breed not in breeds:
        print(f"{breed} not found")
    else:
        cursor.execute('''SELECT * FROM dogs WHERE LOWER(breed) = ?''', (breed,))
        dogs = cursor.fetchall()
        if dogs:
            for dog in dogs:
                print(dog)
        else:
            print("\nNo dogs found")

    # Commit changes to database and close connection
    conn.commit()
    conn.close()

# Searches for the monkey species
def searchBySpecies():
    # Connect to sqlite and create cursor object
    conn = sqlite3.connect('animals.db')
    cursor = conn.cursor()

    eligibleSpecies = ["capuchin", "guenon", "macaque", "marmoset", "squirrel monkey", "tamarin"]
    species = input("Enter monkey species: ").strip().lower()
    if species not in eligibleSpecies:
        print(f"{species} not found")
    else:
        cursor.execute('''SELECT * FROM monkeys WHERE LOWER(species) = ?''', (species,))
        monkeys = cursor.fetchall()
        if monkeys:
            for monkey in monkeys:
                print(monkey)
        else:
            print("\nNo monkeys found")

# Removes a dog or monkey from the respective table
def removeAnimal():
    animalType = input("Enter the animal type you wish to search for (dog or monkey):\n").strip().lower()

    # Input validation for animal type
    while animalType not in ["dog", "monkey"]:
        print("Invalid animal type. Please enter 'dog' or 'monkey':\n")
        animalType = input().strip().lower()
    
    name = input("What is the animal's name?: ")

    # Connect to sqlite and create cursor object
    conn = sqlite3.connect('animals.db')
    cursor = conn.cursor()

    # Check dog or monkey table for animal type and name
    if animalType == "dog":
        cursor.execute('''DELETE FROM dogs WHERE name = ?''', (name,))
    elif animalType == "monkey":
        cursor.execute('''DELETE FROM monkeys WHERE name = ?''', (name,))
    else:
        print(f"No {animalType} found with the name {name}")
        return
    
    # Commit changes to database and close connection
    conn.commit()
    conn.close()

    # Display message that dog was added successfully
    print(name + " was removed")

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
    print("[10] Remove dog or monkey from database")
    print("[q] Quit application\n")
    print("Enter a menu selection:")

# Main method initializes the dog and monkey list, displays menu options, and
# loops until the user enters 'q' to quit the program
def main():

    # Initialize both lists
    createTables()
    populateTestData()

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
        
        elif menuSelection == "10":
            removeAnimal()
        
        elif menuSelection == "q":
            print("The application has been quit.")
            quit = True

        else:
            print("Invalid menu selection")   

main()
