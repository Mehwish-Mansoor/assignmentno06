# 20. Creating a Custom Exception
# Assignment:
# Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception if age < 18. Handle it with try...except.

class InvalidAgeError(Exception):
    """Custom exception for invalid age."""
    def __init__(self, message="Age must be 18 or older."):
        self.message = message
        super().__init__(self.message)

def check_age(age):
    if age < 18:
        raise InvalidAgeError(f"Invalid age: {age}. You must be at least 18 years old.")
    else:
        print("Age is valid.")

# Example usage
if __name__ == "__main__":
    try:
        age = 16  # Example age
        check_age(age)
    except InvalidAgeError as e:
        print(f"Exception caught: {e}")