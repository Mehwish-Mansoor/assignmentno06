# 9. Abstract Classes and Methods
# Assignment:
# Use the abc module to create an abstract class Shape with an abstract method area(). Inherit a class Rectangle that implements area().


from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        # Abstract method to be implemented by subclasses
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        # Implement the abstract method
        return self.width * self.height

# Example usage
if __name__ == "__main__":
    rect = Rectangle(5, 10)
    print(f"Area of the rectangle: {rect.area()}") 