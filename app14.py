# 14. Aggregation
# Assignment:
# Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def display_employee_info(self):
        print(f"Employee Name: {self.name}, Position: {self.position}")

class Department:
    def __init__(self, name, employee):
        self.name = name
        # Aggregation: Department has a reference to an Employee object
        self.employee = employee

    def display_department_info(self):
        print(f"Department: {self.name}")
        self.employee.display_employee_info()

# Example usage
if __name__ == "__main__":
    emp = Employee("Mehwish", "Software Engineer")  # Create an Employee object
    dept = Department("IT", emp)  # Pass the Employee object to the Department class
    dept.display_department_info()