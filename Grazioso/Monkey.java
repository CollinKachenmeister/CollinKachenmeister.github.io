public class Monkey extends RescueAnimal {
    // Private attributes
    private String tailLength;
    private String height;
    private String bodyLength;
    private String species;

    // Constructor
    public Monkey(String name, String species, String tailLength, String height, String bodyLength,
                  String gender, String age, String weight, String acquisitionDate, String acquisitionCountry,
                  String trainingStatus, boolean reserved, String inServiceCountry, String animalType) {
        setName(name);
        setSpecies(species);
        setTailLength(tailLength);
        setHeight(height);
        setBodyLength(bodyLength);
        setGender(gender);
        setAge(age);
        setWeight(weight);
        setAcquisitionDate(acquisitionDate);
        setAcquisitionLocation(acquisitionCountry);
        setTrainingStatus(trainingStatus);
        setReserved(reserved);
        setInServiceCountry(inServiceCountry);
        setAnimalType(animalType);
    }

    // Mutator methods
    public void setTailLength(String tailLength) {
        this.tailLength = tailLength;
    }
    public void setHeight(String height) {
        this.height = height;
    }
    public void setBodyLength(String bodyLength) {
        this.bodyLength = bodyLength;
    }
    public void setSpecies(String species) {
        this.species = species;
    }

    // Accessor methods
    public String getTailLength() {
        return tailLength;
    }
    public String getHeight() {
        return height;
    }
    public String getBodyLength() {
        return bodyLength;
    }
    public String getSpecies() {
        return species;
    }
}
