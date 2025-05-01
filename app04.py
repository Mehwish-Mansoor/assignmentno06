
# 4. Class Variables and Class Methods
# Assignment:
# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.

class Bank:
    # Class variable to store the bank name
    bank_name = "Default Bank"

    @classmethod
    def change_bank_name(cls, name):
        # Class method to change the bank name
        cls.bank_name = name

# Example usage
if __name__ == "__main__":
    # Access the class variable through the class
    print(f"Initial Bank Name: {Bank.bank_name}")

    # Change the bank name using the class method
    Bank.change_bank_name("Global Bank")

    # Access the updated class variable through the class
    print(f"Updated Bank Name: {Bank.bank_name}")

    # Create instances and show that the change affects all instances
    account1 = Bank()
    account2 = Bank()
    print(f"Account1 Bank Name: {account1.bank_name}")
    print(f"Account2 Bank Name: {account2.bank_name}")