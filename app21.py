# 21. Make a Custom Class Iterable
# Assignment:
# Create a class Countdown that takes a start number. Implement __iter__() and __next__() to make the object iterable in a for-loop, counting down to 0.

# Once you are done submit this form ASAP

class Countdown:
    def __init__(self, start):
        self.current = start  # Initialize the starting number

    def __iter__(self):
        # Return the iterator object (self in this case)
        return self

    def __next__(self):
        # Define the logic for iteration
        if self.current < 0:
            raise StopIteration  # Stop iteration when the countdown reaches below 0
        else:
            value = self.current
            self.current -= 1  # Decrement the current value
            return value

# Example usage
if __name__ == "__main__":
    countdown = Countdown(5)  # Create a Countdown object starting from 5
    for number in countdown:
        print(number)  # Output: 5, 4, 3, 2, 1, 0