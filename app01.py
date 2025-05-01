# 1. Using self
# Assignment:
# Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. Add a method display() that prints student details.

class Student:
    def __init__(self, name, marks):
        # Initialize attributes using self
        self.name = name
        self.marks = marks

    def display(self):
        # Display student details
        print(f"Name: {self.name}, Marks: {self.marks}")

# Example usage
if __name__ == "__main__":
    student1 = Student("Mehwish", 88)
    student1.display()