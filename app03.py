# 3. Public Variables and Methods
# Assignment:
# Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.

class Car:
    def __init__(self, brand):
        # Public variable
        self.brand = brand

    # Public method
    def start(self):
        print(f"The {self.brand} car has started.")

# Example usage
if __name__ == "__main__":
    my_car = Car("Toyota")  # Instantiate the class
    print(my_car.brand)     # Access the public variable
    my_car.start()          # Call the public method