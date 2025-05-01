# 5. Static Variables and Static Methods
# Assignment:
# Create a class MathUtils with a static method add(a, b) that returns the sum. No class or instance variables should be used

class MathUtils:
    @staticmethod
    def add(a, b):
        # Static method to return the sum of two numbers
        return a + b

# Example usage
if __name__ == "__main__":
    result = MathUtils.add(25, 17)  # Call the static method without creating an instance
    print(f"The sum is: {result}")  # Output: The sum is: 12