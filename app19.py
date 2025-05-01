# 19. callable() and __call__()
# Assignment:
# Create a class Multiplier with an __init__() to set a factor. Define a __call__() method that multiplies an input by the factor. Test it with callable() and by calling the object like a function.

class Multiplier:
    def __init__(self, factor):
        self.factor = factor  # Set the multiplication factor

    def __call__(self, value):
        # Multiply the input value by the factor
        return value * self.factor

# Example usage
if __name__ == "__main__":
    multiplier = Multiplier(5)  # Create a Multiplier object with factor 5

    # Test if the object is callable
    print(callable(multiplier))  # Output: True

    # Call the object like a function
    result = multiplier(10)  # Multiply 10 by the factor (5)
    print(result)  # Output: 50