# 2. Using cls
# Assignment:
# Create a class Counter that keeps track of how many objects have been created. Use a class variable and a class method with cls to manage and display the count.

class Counter:
    # Class variable to keep track of the count
    count = 0

    def __init__(self):
        # Increment the count whenever an object is created
        Counter.count += 1

    @classmethod
    def display_count(cls):
        # Class method to display the count
        print(f"Number of objects created: {cls.count}")

# Example usage
if __name__ == "__main__":
    obj1 = Counter()
    obj2 = Counter()
    obj3 = Counter()
    obj4 = Counter()
    obj5 = Counter()
    obj6 = Counter()
    Counter.display_count()  # Output: Number of objects created: 3