"""
Python Fundamentals - 10 Functions
Description: Functions are reusable blocks of code.
This file covers defining functions, parameters, return values, and docstrings.
"""

# ==========================================
# 1. Basic Function Definition
# ==========================================
# Use the 'def' keyword.
# Good practice: Function names should be verbs (e.g., calculate_sum, get_user).

def greet_user():
    """Prints a welcome message to the user."""
    print("Hello! Welcome to the Python Fundamentals course.")

print("--- Basic Function Call ---")
greet_user()  # Calling the function

# ==========================================
# 2. Parameters and Arguments
# ==========================================
# Passing data INTO the function.

def greet_person(name, department):
    print(f"Hello {name}, welcome to {department} department.")

print("\n--- Function with Parameters ---")
greet_person("Sema", "Computer Engineering")

# ==========================================
# 3. Return Statement (Crucial!)
# ==========================================
# 'print' just shows text on screen. 'return' gives the data back to the code.
# In engineering, 99% of functions should RETURN data, not print it.

def calculate_square(number):
    result = number * number
    return result

print("\n--- Return Values ---")
my_num = 5
squared_val = calculate_square(my_num) # Capture the returned value in a variable
print(f"The square of {my_num} is: {squared_val}")


# ==========================================
# 4. Default Parameters
# ==========================================
# If the user doesn't provide a value, use a default one.
# Useful for API configurations or Data Science settings.

def power(number, exponent=2):
    """
    Calculates number to the power of exponent.
    Default exponent is 2 (Square).
    """
    return number ** exponent

print("\n--- Default Parameters ---")
print("Power(5) [Default]:", power(5))      # Uses exponent=2 -> 25
print("Power(5, 3) [Custom]:", power(5, 3)) # Uses exponent=3 -> 125