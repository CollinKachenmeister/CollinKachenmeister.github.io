import java.util.ArrayList;
import java.util.Scanner;

public class Driver {
    private static ArrayList<Dog> dogList = new ArrayList<Dog>();          // Create new ArrayList for dog
    private static ArrayList<Monkey> monkeyList = new ArrayList<Monkey>(); // Create new ArrayList for monkey

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        boolean quit = false; // Variable to exit menu loop

        initializeDogList();
        initializeMonkeyList();

        // Menu loop displays menu after each input and prompts user for input
        while (!quit) {
            displayMenu(); // Displays menu after input

            String menuSelection = scanner.nextLine(); // Variable for user input for menu selection in the loop

            switch (menuSelection) {
                case "1":  // Intakes a new dog
                    intakeNewDog(scanner);
                    break;

                case "2":  // Intakes a new monkey
                    intakeNewMonkey(scanner);
                    break;

                case "3":  // Reserves an animal
                    reserveAnimal(scanner);
                    break;

                case "4":  // Prints a list of all dogs
                    printAnimals("Dog");
                    break;

                case "5":  // Prints a list of all monkeys
                    printAnimals("Monkey");
                    break;

                case "6": // Prints a list of all animals that are not reserved
                    printAnimals("Available");
                    break;

                case "q": // Allows user to quit the application
                    System.out.println("The application has been quit.");
                    quit = true;
                    break;

                default: // Input validation
                    System.out.println("Invalid menu selection");

            }

        }
    }

    // This method prints the menu options
    public static void displayMenu() {
        System.out.println("\n\n");
        System.out.println("\t\t\t\tRescue Animal System Menu");
        System.out.println("[1] Intake a new dog");
        System.out.println("[2] Intake a new monkey");
        System.out.println("[3] Reserve an animal");
        System.out.println("[4] Print a list of all dogs");
        System.out.println("[5] Print a list of all monkeys");
        System.out.println("[6] Print a list of all animals that are not reserved");
        System.out.println("[q] Quit application");
        System.out.println();
        System.out.println("Enter a menu selection");
    }


    // Adds dogs to a list for testing
    public static void initializeDogList() {
        Dog dog1 = new Dog("Spot", "German Shepherd", "male", "1", "25.6", "05-12-2019", "United States", "intake", false, "United States", "Dog");
        Dog dog2 = new Dog("Rex", "Great Dane", "male", "3", "35.2", "02-03-2020", "United States", "Phase I", false, "United States", "Dog");
        Dog dog3 = new Dog("Bella", "Chihuahua", "female", "4", "25.6", "12-12-2019", "Canada", "in service", true, "Canada", "Dog");

        dogList.add(dog1);
        dogList.add(dog2);
        dogList.add(dog3);
    }


    // Adds monkeys to a list for testing
    public static void initializeMonkeyList() {
        Monkey monkey1 = new Monkey("Fred", "Capuchin", "10.2", "30.4", "25.6", "male", "5", "28.7", "05-12-2019", "United States", "intake", false, "United States", "Monkey");
        Monkey monkey2 = new Monkey("Winston", "Guenon", "15.6", "35.9", "35.2", "male", "4", "30.7", "02-03-2020", "United States", "Phase I", true, "United States", "Monkey");
        Monkey monkey3 = new Monkey("Bananas", "Macaque", "20.8", "40.8", "25.6", "female", "3","24.6", "12-12-2019", "Canada", "in service", false, "Canada", "Monkey");

        monkeyList.add(monkey1);
        monkeyList.add(monkey2);
        monkeyList.add(monkey3);
    }


    // Method prompts user for relevant data and sets data for all attributes
    // then adds the newly instantiated dog to dogList
    // Includes input validation for duplicate names in dogList
    public static void intakeNewDog(Scanner scanner) {
        System.out.println("What is the dog's name?");
        String name = scanner.nextLine();
        for(Dog dog: dogList) {
            if (dog.getName().equalsIgnoreCase(name)) {
                System.out.println("\n\nThis dog is already in our system\n\n");
                return; //returns to menu if dog name is already in dogList
            }
        }
            // Prompts the user to input the dog's breed
            System.out.println("What is the dog's breed?");
            String breed = scanner.nextLine();

            // Prompts user to input dog's gender
            System.out.println("What is the dog's gender?");
            String gender = scanner.nextLine();

            // Prompts user to input dog's age
            System.out.println("What is the dog's age?");
            String age = scanner.nextLine();

            // Prompts user to input dog's weight
            System.out.println("What is the dog's weight?");
            String weight = scanner.nextLine();

            // Prompts user to input dog's acquisition date
            System.out.println("What is the dog's acquisition date?");
            String acquisitionDate = scanner.nextLine();

            // Prompts user to input dog's acquisition country
            System.out.println("What is the dog's acquisition country?");
            String acquisitionCountry = scanner.nextLine();

            // Prompts user to input dog's training status
            System.out.println("What is the dog's training status?");
            String trainingStatus = scanner.nextLine();

            // Prompts user to input if dog is reserved or not
            System.out.println("Is the dog reserved? (true or false)");
            boolean reserved = scanner.nextBoolean();
            scanner.nextLine();  // allows the scanner to input a new string

            // Prompts user for the dog's service country
            System.out.println("What is the dog's service country?");
            String inServiceCountry = scanner.nextLine();

            // Sets animalType to Dog
            String animalType = "Dog";

            // Adds user input information to dogList
            dogList.add(new Dog(name, breed, gender, age, weight, acquisitionDate, acquisitionCountry,
                    trainingStatus, reserved, inServiceCountry, animalType));

            // Outputs that the dog was added to the dog list
            System.out.println(name + " was added to the list");
    }
        // Method prompts user for relevant data and sets data for all attributes
        // then adds the newly instantiated monkey to monkeyList
        // Includes input validation for duplicate names in monkeyList and validates species
        public static void intakeNewMonkey(Scanner scanner) {
            // Prompts user to input monkey's name
            System.out.println("What is the monkey's name?");
            String name = scanner.nextLine();
            for(Monkey monkey: monkeyList) {  // Input validation iterates through list to check if monkey name already exits
                if(monkey.getName().equalsIgnoreCase(name)) {
                    System.out.println("\n\nThis monkey is already in our system\n\n");
                    return; // returns to menu if monkey name is already in monkeyList
                }
            }
            // Prompts user to input monkey's species
            System.out.println("What is the monkey's species?");
            String species = scanner.nextLine();
            // Input validation checks if user input species is eligible for training
            if(!species.equalsIgnoreCase("capuchin") && !species.equalsIgnoreCase("guenon")
                    && !species.equalsIgnoreCase("macaque") && !species.equalsIgnoreCase("marmoset")
                    && !species.equalsIgnoreCase("squirrel monkey") && !species.equalsIgnoreCase("tamarin")) {
                System.out.println("\n\nThis species of monkey is not eligible for training\n\n");
                return; // returns to menu if species is not available for training
            }
            // Prompts user to input monkey's tail length
            System.out.println("What is the monkey's tail length?");
            String tailLength = scanner.nextLine();

            // Prompts user to input monkey's height
            System.out.println("What is the monkey's height?");
            String height = scanner.nextLine();

            // Prompts user to input monkey's body length
            System.out.println("What is the monkey's body length?");
            String bodyLength = scanner.nextLine();

            // Prompts user to input monkey's gender
            System.out.println("What is the monkey's gender?");
            String gender = scanner.nextLine();

            // Prompts user to input monkey's age
            System.out.println("What is the monkey's age?");
            String age = scanner.nextLine();

            // Prompts user to input monkey's weight
            System.out.println("What is the monkey's weight?");
            String weight = scanner.nextLine();

            // Prompts user to input monkey's acquisition date
            System.out.println("What is the monkey's acquisition date?");
            String acquisitionDate = scanner.nextLine();

            // Prompts user to input monkey's acquisition country
            System.out.println("What is the monkey's acquisition country?");
            String acquisitionCountry = scanner.nextLine();

            // Prompts user to input monkey's training status
            System.out.println("What is the monkey's training status?");
            String trainingStatus = scanner.nextLine();

            // Prompts user to input if monkey is reserved or not
            System.out.println("Is the monkey reserved? (true or false)");
            boolean reserved = scanner.nextBoolean();
            scanner.nextLine();  // allows the scanner to input a new string

            // Prompts user for the monkey's service country
            System.out.println("What is the monkey's service country?");
            String inServiceCountry = scanner.nextLine();

            // Set animalType to Monkey
            String animalType = "Monkey";

            // Adds user input monkey information to monkeyList
            monkeyList.add(new Monkey(name, species, tailLength, height, bodyLength,
                    gender, age, weight, acquisitionDate, acquisitionCountry,
                    trainingStatus, reserved, inServiceCountry, animalType));

            // Outputs that the monkey was added to the monkey list
            System.out.println(name + " was added to the list");
        }

        // Method sets reserved status to true for the first animal found in ArrayList
        // if the animal is not reserved and exists in the user input in-service country
        public static void reserveAnimal(Scanner scanner) {
            // Prompt user for animal type
            System.out.println("Enter the animal type you wish to search for (dog or monkey):");
            String animalType = scanner.nextLine();

            // Loops until valid animal type is input
            while (!animalType.equalsIgnoreCase("dog") && !animalType.equalsIgnoreCase("monkey")) {
                System.out.println("Invalid animal type. Please enter 'dog' or 'monkey'.");
                animalType = scanner.nextLine();
            }

            // Prompt user for animal's in-service country
            System.out.println("Enter the animal's in-service country");
            String inServiceCountry = scanner.nextLine();

            // Checks if animalType is dog or monkey
            // Iterates through the appropriate list finding user input in-service country
            // and checks if the animal is reserved or not
            // If both criteria are met, sets the reserved status to true for the first input animal type found in the list
            boolean found = false;
            if (animalType.equalsIgnoreCase("dog")) {
                for (int i = 0; i < dogList.size(); ++i) {
                    if (dogList.get(i).getInServiceLocation().equalsIgnoreCase(inServiceCountry) && !dogList.get(i).getReserved()) {
                        dogList.get(i).setReserved(true);
                        System.out.println(dogList.get(i).getName() + " was reserved.");
                        return;     // returns to the menu so that only the first dog that meets the criteria is reserved
                    }
                }
                if (!found) {       // Error message if no dogs are found
                    System.out.println("No " + animalType + " is available in " + inServiceCountry);
                }
            }
            if (animalType.equalsIgnoreCase("monkey")) {
                for (int i = 0; i < monkeyList.size(); ++i) {
                    if (monkeyList.get(i).getInServiceLocation().equalsIgnoreCase(inServiceCountry) && !monkeyList.get(i).getReserved()) {
                        monkeyList.get(i).setReserved(true);
                        System.out.println(monkeyList.get(i).getName() + " was reserved.");
                        return;     // returns to menu so that only the first monkey that meets the criteria is reserved
                    }
                }
                if (!found) {       // Error message if no monkeys are found
                    System.out.println("No " + animalType + " is available in " + inServiceCountry);
                }
            }
        }

        // The printAnimals() method has three different outputs
        // based on the listType parameter
        // dog - prints the list of dogs
        // monkey - prints the list of monkeys
        // available - prints a combined list of all animals that are
        // fully trained ("in service") but not reserved
        public static void printAnimals(String listType) {
            boolean found = false;          // flag used to output no available animals
            if (listType.equals("Dog")) {        // Outputs list of all dogs
                System.out.println("List of dogs");
                for (Dog dog: dogList) {   // Iterates through dogList and outputs relevant data
                    System.out.println("Name: " + dog.getName() + ", status: " + dog.getTrainingStatus() + ", acquisition country: " + dog.getAcquisitionLocation() + ", reserved: " + dog.getReserved());
                }
            }
            else if (listType.equals("Monkey")) {        // Outputs list of all monkeys
                System.out.println("List of monkeys");
                for (Monkey monkey: monkeyList) {  // Iterates through monkeyList and outputs relevant data
                    System.out.println("Name :" + monkey.getName() + ", status: " + monkey.getTrainingStatus() + ", acquisition country: " + monkey.getAcquisitionLocation() + ", reserved: " + monkey.getReserved());
                }
            }
            else if (listType.equals("Available")) {     // Outputs list of all animals in service and not reserved
                for (Dog dog: dogList) {           // Iterates through dog list and outputs dogs that are in service and not reserved
                    if (dog.getTrainingStatus().equalsIgnoreCase("in service") && !dog.getReserved()) {
                        System.out.println("Animal type: " + dog.getAnimalType() + ", name: " + dog.getName() + ", status: " + dog.getTrainingStatus() + ", acquisition country: " + dog.getAcquisitionLocation() + ", reserved: " + dog.getReserved());
                        found = true;
                    }
                }
                for (Monkey monkey: monkeyList) {  // Iterates through monkey list and outputs monkeys that are in service and not reserved
                    if (monkey.getTrainingStatus().equalsIgnoreCase("in service") && !monkey.getReserved()) {
                        System.out.println("Animal type: " + monkey.getAnimalType() + ", name: " + monkey.getName() + ", status: " + monkey.getTrainingStatus() + ", acquisition country: " + monkey.getAcquisitionLocation() + ", reserved: " + monkey.getReserved());
                        found = true;
                    }
                }
                if (!found) {       // Output if no animals are in-service and not reserved
                    System.out.println("No animals are in service and not reserved");
                }
            }
        }
}

