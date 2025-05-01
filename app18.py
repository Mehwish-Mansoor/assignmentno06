# 18. Property Decorators: @property, @setter, and @deleter
# Assignment:
# Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.

class Product:
    def __init__(self, price):
        self._price = price  # Private attribute

    @property
    def price(self):
        # Getter method for price
        return self._price

    @price.setter
    def price(self, value):
        # Setter method for price
        if value >= 0:
            self._price = value
        else:
            raise ValueError("Price cannot be negative!")

    @price.deleter
    def price(self):
        # Deleter method for price
        print("Deleting price...")
        del self._price

# Example usage
if __name__ == "__main__":
    product = Product(100)  # Create a Product object with price 100
    print(product.price)    # Output: 100 (getter is called)

    product.price = 150     # Update the price (setter is called)
    print(product.price)    # Output: 150

    del product.price       # Delete the price (deleter is called)