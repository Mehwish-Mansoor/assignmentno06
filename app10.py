# 10. Instance Methods
# Assignment:
# Create a class Dog with instance variables name and breed. Add an instance method bark() that prints a message including the dog's name.

class Dog:
    def __init__(self, name, breed):
        # Instance variables
        self.name = name
        self.breed = breed

    def bark(self):
        # Instance method
        print(f"{self.name}, the {self.breed}, says: Woof! Woof!")

# Example usage
if __name__ == "__main__":
    my_dog = Dog("Buddy",  "German Shepherd")
    my_dog.bark()  # Output: Buddy, the Golden Retriever, says: Woof! Woof!