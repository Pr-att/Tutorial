# Encapsulation
# Inheritance
# Polymorphism
# Abstraction

# Encapsulation: It is process of binding data and functions together in a single unit.

class Animal:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def get_age(self):
        return self.__age

    def speak(self):
        print(f"I am {self.name} and I am {self.age} years old.")


obj1 = Animal("Rony", 7)
print(obj1.get_age())

# Inheritance: It is a process of acquiring properties of one class by another class.


class Dog(Animal):
    def __init__(self, name, age, breed) -> None:
        super().__init__(name, age)
        self.breed = breed

    def speak(self):
        print(
            f"I am {self.name} and I am {self.age} years old. I am a {self.breed}.")


obj2 = Dog("Tom", 10, "German Shepherd")
obj2.speak()

# Polymorphism: It is a process of using same function in different ways.

# Abstraction: It is a process of hiding the implementation details from the user.


class Animal:
    def __init__(self, name, age) -> None:
        self.name = name
        self.__age = age  # Private variable
        # self._age = age # Protected variable

    def get_age(self):
        return self.__age

    def speak(self):
        print(f"I am {self.name} and I am {self.age} years old.")


obj1 = Animal("Rony", 7)
print(obj1.get_age())
