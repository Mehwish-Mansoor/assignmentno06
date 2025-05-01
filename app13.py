
# 13. Composition
# Assignment:
# Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. Access a method of the Engine class via the Car class


class Engine:
    def start(self):
        print("Engine has started.")

class Car:
    def __init__(self, engine):
        # Composition: Car has an Engine
        self.engine = engine

    def start_car(self):
        # Accessing the Engine's method via the Car class
        self.engine.start()

# Example usage
if __name__ == "__main__":
    engine = Engine()  # Create an Engine object
    car = Car(engine)  # Pass the Engine object to the Car class
    car.start_car()    # Output: Engine has started.