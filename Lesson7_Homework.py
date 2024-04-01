import json

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print("Some generic sound")

    def eat(self):
        print(f"{self.name} is eating.")

class Bird(Animal):
    def make_sound(self):
        print(f"{self.name} says: Чирик!")

class Mammal(Animal):
    def make_sound(self):
        print(f"{self.name} says: Му-у!")

class Reptile(Animal):
    def make_sound(self):
        print(f"{self.name} says: Ш-ш-ш!")

class Zookeeper:
    def __init__(self, name):
        self.name = name

    def feed_animals(self, animals):
        for animal in animals:
            print(f"{self.name} feeds {animal.name}.")

class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animals(self, animals):
        for animal in animals:
            print(f"{self.name} is treating {animal.name}.")

class Zoo:
    def __init__(self):
        self.animals = []
        self.staff_list = []

    def add_animal(self, animal):
        if isinstance(animal, Animal):
            self.animals.append(animal)
            print(f"{animal.name} has been added to the zoo.")

    def add_staff(self, staff):
        self.staff_list.append(staff)
        print(f"{staff.name} has been added to the zoo staff.")

    def save_to_file(self, filename):
        zoo_data = {
            "animals": [{"name": animal.name, "type": animal.__class__.__name__, "age": animal.age} for animal in self.animals],
            "staff": [{"name": staff.name, "type": staff.__class__.__name__} for staff in self.staff_list]
        }
        with open(filename, 'w') as file:
            json.dump(zoo_data, file)

    def load_from_file(self, filename):
        with open(filename, 'r') as file:
            zoo_data = json.load(file)
            for animal_data in zoo_data["animals"]:
                animal = self.create_animal(animal_data["name"], animal_data["type"], animal_data["age"])
                self.animals.append(animal)
            for staff_data in zoo_data["staff"]:
                # Assuming all staff are Zookeepers for simplicity
                staff = Zookeeper(staff_data["name"])
                self.staff_list.append(staff)

    def create_animal(self, name, type, age):
        if type == "Bird":
            return Bird(name, age)
        elif type == "Mammal":
            return Mammal(name, age)
        elif type == "Reptile":
            return Reptile(name, age)
        else:
            return Animal(name, age)

# Demonstrating functionality
zoo = Zoo()
zoo.add_animal(Bird("Parrot", 2))
zoo.add_animal(Mammal("Lion", 3))
zoo.add_staff(Zookeeper("Alex"))

# Save to file
zoo.save_to_file("zoo_data.json")

# Load from file and demonstrate
new_zoo = Zoo()
new_zoo.load_from_file("zoo_data.json")
for animal in new_zoo.animals:
    print(f"Loaded {animal.name} the {animal.__class__.__name__}, aged {animal.age}")
for staff in new_zoo.staff_list:
    print(f"Loaded staff member {staff.name} the {staff.__class__.__name__}")
