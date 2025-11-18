"""
Python Fundamentals - 02 Operators
Description: This file covers Arithmetic, Comparison, and Logical operators.
It also demonstrates Floor Division and Modulus concepts.
"""

# ==========================================
# 1. Arithmetic Operators
# ==========================================
a = 10
b = 3

print("--- Arithmetic Operations ---")
print(f"Addition ({a} + {b}):", a + b)
print(f"Subtraction ({a} - {b}):", a - b)
print(f"Multiplication ({a} * {b}):", a * b)
print(f"Division ({a} / {b}):", a / b)       # Returns float

# Special Python Operators
print(f"Floor Division ({a} // {b}):", a // b) # Returns integer (cuts decimal part)
print(f"Modulus ({a} % {b}):", a % b)          # Returns the remainder (Useful for even/odd checks)
print(f"Exponentiation ({a} ** {b}):", a ** b) # Power (10^3)


# ==========================================
# 2. Comparison Operators
# ==========================================
# These always return a Boolean (True or False).

x = 5
y = 10

print("\n--- Comparison Operations ---")
print(f"Is {x} equal to {y}? (x == y):", x == y)
print(f"Is {x} not equal to {y}? (x != y):", x != y)
print(f"Is {x} greater than {y}? (x > y):", x > y)
print(f"Is {x} less than {y}? (x < y):", x < y)


# ==========================================
# 3. Logical Operators
# ==========================================
# Used to combine conditional statements: and, or, not

is_student = True
has_laptop = True
is_tired = False

print("\n--- Logical Operations ---")
# 'and': Returns True if both statements are true
print("Can study? (is_student and has_laptop):", is_student and has_laptop)

# 'or': Returns True if one of the statements is true
print("Needs break? (is_tired or is_student):", is_tired or is_student)

# 'not': Reverse the result
print("Is NOT tired?:", not is_tired)


# ==========================================
# 4. Assignment Operators (Shortcuts)
# ==========================================
# Shortcuts for updating variables (Counter logic)

counter = 0
counter += 1  # Same as: counter = counter + 1
print(f"\nCounter after increment: {counter}")

counter *= 5  # Same as: counter = counter * 5
print(f"Counter after multiplication: {counter}")