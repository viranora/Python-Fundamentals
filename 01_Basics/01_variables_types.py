"""
Python Fundamentals - 01 Variables & Data Types
Description: This file demonstrates basic data types in Python, 
variable naming conventions, and type casting.
"""

# ==========================================
# 1. Variable Assignment
# ==========================================
# Python is dynamically typed (no need to declare types explicitly).
# Use 'snake_case' for variable names (lowercase with underscores).

student_name = "Sema"           # String
student_age = 22                # Integer
gpa = 3.45                      # Float
is_intern = True                # Boolean (True/False)

print("--- Student Information ---")
print("Name:", student_name)
print("Age:", student_age)
print("GPA:", gpa)
print("Is Intern?:", is_intern)


# ==========================================
# 2. Type Checking
# ==========================================
# The type() function returns the class type of the object.
# Useful for debugging and data validation in Data Science.

print("\n--- Data Types (Type Checking) ---")
print(f"Type of '{student_name}': {type(student_name)}")
print(f"Type of '{student_age}': {type(student_age)}")
print(f"Type of '{gpa}': {type(gpa)}")
print(f"Type of '{is_intern}': {type(is_intern)}")


# ==========================================
# 3. Type Casting (Conversion)
# ==========================================
# Converting variables from one data type to another.
# Example: Input often comes as a string ("25"), needs conversion to int for math.

str_number = "100"
int_number = int(str_number)     # Convert String to Integer
float_number = float(str_number) # Convert String to Float

print("\n--- Type Casting ---")
print("Original String:", str_number)
print("Converted to Integer:", int_number, "| Type:", type(int_number))
print("Converted to Float:", float_number, "| Type:", type(float_number))

# ==========================================
# 4. Multiple Assignment
# ==========================================
# Assign values to multiple variables in one line (Pythonic Way).

x, y, z = 10, 20, 30
print(f"\nx: {x}, y: {y}, z: {z}")