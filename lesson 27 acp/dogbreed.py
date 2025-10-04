class Dog:
    # Class variable
    animal = "Dog"

    # Constructor with instance variables
    def __init__(self, breed, colour):
        self.breed = breed
        self.colour = colour


# Create two Dog objects
dog1 = Dog("Labrador", "Golden")
dog2 = Dog("German Shepherd", "Black and Tan")

# Display details
print(f"Animal: {dog1.animal}")
print(f"Breed: {dog1.breed}, Colour: {dog1.colour}")

print(f"\nAnimal: {dog2.animal}")
print(f"Breed: {dog2.breed}, Colour: {dog2.colour}")
