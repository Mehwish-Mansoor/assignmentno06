# 8. The super() Function
# Assignment:
# Create a class Person with a constructor that sets the name. Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor.

class Person:
    def __init__(self, name):
        # Constructor to set the name
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        # Use super() to call the base class constructor
        super().__init__(name)
        self.subject = subject

    def display_info(self):
        print(f"Teacher Name: {self.name}")
        print(f"Subject: {self.subject}")

# Example usage
if __name__ == "__main__":
    t = Teacher("Mehwish", "Computer")
    t.display_info()