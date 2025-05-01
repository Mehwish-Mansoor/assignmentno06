# 7. Access Modifiers: Public, Private, and Protected
# Assignment:
# Create a class Employee with:

# a public variable name,

# a protected variable _salary, and

# a private variable __ssn.

# Try accessing all three variables from an object of the class and document what happens

class Employee:
    def __init__(self, name, salary, ssn):
        # Public variable
        self.name = name
        # Protected variable
        self._salary = salary
        # Private variable
        self.__ssn = ssn

    def get_ssn(self):
        return self.__ssn

    def set_salary(self, new_salary):
        if new_salary > 0:
            self._salary = new_salary
        else:
            print("Salary must be positive numbers.")

    def display_info(self):
        # Accessing all variables within the class
        print(f"Name: {self.name}, Salary: {self._salary}, SSN: {self.__ssn}")


class Manager(Employee):
    def __init__(self, name, salary, ssn, department):
        super().__init__(name, salary, ssn)
        self.department = department

    def show_manager_info(self):
        print(f"Manager: {self.name}")
        print(f"Department: {self.department}")
        print(f"Protected Salary: {self._salary}")
        print(f"Accessing SSN via getter command: {self.get_ssn()}")


# Example usage
if __name__ == "__main__":
    m = Manager("Mehwish", 30000, "123-45-6789", "HR")
    m.show_manager_info()
    m.set_salary(45000)
    print("Updated Salary:", m._salary)
    print("Private SSN via getter:", m.get_ssn())