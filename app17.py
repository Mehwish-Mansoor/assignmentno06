# 17. Class Decorators
# Assignment:
# Create a class decorator add_greeting that modifies a class to add a greet() method returning "Hello from Decorator!". Apply it to a class Person.


def add_greeting(cls):
    # Add a greet method to the class
    cls.greet = lambda self: "Hello from Decorator!"
    return cls

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Example usage
if __name__ == "__main__":
    person = Person("Alice")
    print(person.greet())  