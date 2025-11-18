"""
Python Fundamentals - 13 Classes & Objects (OOP Intro)
Description: 
- Class: The blueprint/template for creating objects.
- Object: An instance of a class.
- __init__: The constructor method (runs automatically when creating an object).
- self: Represents the instance itself.
"""

# ==========================================
# 1. Defining a Class
# ==========================================

class SoftwareEngineer:
    
    # Class Attribute: Same for ALL objects of this class
    job_title = "Software Engineer"

    # The Constructor (__init__)
    # This runs automatically when you create a new object.
    # 'self' is a reference to the specific object being created.
    def __init__(self, name, level, salary):
        # Instance Attributes: Unique to EACH object
        self.name = name
        self.level = level   # Junior, Mid, Senior
        self.salary = salary

    # Instance Method (Action)
    def code(self):
        print(f"{self.name} is writing code...")

    def code_in_language(self, language):
        print(f"{self.name} is coding in {language}...")
    
    def get_info(self):
        return f"Name: {self.name}, Level: {self.level}, Salary: ${self.salary}"


# ==========================================
# 2. Creating Objects (Instantiation)
# ==========================================

print("--- Creating Objects ---")
# We use the blueprint (Class) to build engineers (Objects)

se1 = SoftwareEngineer("Sema", "Junior", 5000)
se2 = SoftwareEngineer("Ali", "Senior", 9000)

print(f"Engineer 1: {se1.name}")
print(f"Engineer 2: {se2.name}")


# ==========================================
# 3. Calling Methods
# ==========================================

print("\n--- Calling Methods ---")
se1.code()                  # Sema is writing code...
se2.code_in_language("Python") # Ali is coding in Python...


# ==========================================
# 4. Class Attributes vs Instance Attributes
# ==========================================

print("\n--- Attributes ---")
# Instance attribute (Unique)
print(f"{se1.name}'s Level: {se1.level}")

# Class attribute (Shared)
print(f"SE1 Title: {se1.job_title}") 
print(f"SE2 Title: {se2.job_title}")

# Interesting Fact: Creating a totally generic object
# print(type(se1)) -> <class '__main__.SoftwareEngineer'>