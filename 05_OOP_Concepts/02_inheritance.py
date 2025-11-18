"""
Python Fundamentals - 14 Inheritance
Description: 
- Inheritance: Child class inherits attributes and methods from Parent class.
- super(): Function to call the Parent's methods (especially __init__).
- Method Overriding: Child class modifies the behavior of a Parent method.
"""

# ==========================================
# 1. Parent Class (Base Class)
# ==========================================
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        print(f"{self.name} is working on general tasks.")

    def show_info(self):
        return f"Employee: {self.name}, Salary: ${self.salary}"


# ==========================================
# 2. Child Class (Derived Class)
# ==========================================
# 'Developer' inherits from 'Employee'
# It has everything Employee has, plus more.

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        # Initialize the Parent attributes using super()
        super().__init__(name, salary)
        # Initialize the Child's specific attribute
        self.programming_language = programming_language

    # METHOD OVERRIDING (Polymorphism)
    # We change how 'work' behaves for Developers
    def work(self):
        print(f"{self.name} is writing code in {self.programming_language}.")


# ==========================================
# 3. Another Child Class
# ==========================================

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def work(self):
        print(f"{self.name} is managing a team of {self.team_size} people.")


# ==========================================
# 4. Testing the Hierarchy
# ==========================================

print("--- Inheritance Demo ---")

dev = Developer("Sema", 6000, "Python")
mgr = Manager("Ali", 9000, 10)

# Using inherited method 'show_info' (Defined in Employee, used by Child)
print(dev.show_info())
print(mgr.show_info())

print("\n--- Method Overriding ---")
# Same method name 'work()', but different behaviors (Polymorphism)
dev.work()  # Writes code
mgr.work()  # Manages team

# Checking relationships
# isinstance(object, class) -> Returns True if object belongs to that class
print(f"\nIs Sema a Developer? {isinstance(dev, Developer)}") # True
print(f"Is Sema an Employee? {isinstance(dev, Employee)}")   # True (Because inheritance)