"""
Python Fundamentals - 03 User Input
Description: This file demonstrates how to take input from the user,
handle data types, and perform basic calculations with user data.
"""

# ==========================================
# 1. Basic String Input
# ==========================================
# The input() function pauses the program and waits for the user to type something.
# It ALWAYS returns a string, even if the user types a number.

print("--- User Registration ---")
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

print(f"Welcome, {first_name} {last_name}!")


# ==========================================
# 2. Input with Type Casting (Numbers)
# ==========================================
# Since input() returns a string, we must cast it to int or float for math.

current_year = 2025

# Step-by-step conversion (Safe way)
birth_year_str = input("\nEnter your birth year (e.g., 2003): ")
birth_year = int(birth_year_str) # Converting string "2003" to integer 2003

# One-line conversion (Professional way)
# height = float(input("Enter your height in meters (e.g., 1.75): "))


# ==========================================
# 3. Dynamic Calculation
# ==========================================
# Now we can use the converted variables in calculations.

age = current_year - birth_year

print("\n--- Summary ---")
print(f"User: {first_name}")
print(f"Birth Year: {birth_year}")
print(f"Calculated Age: {age}")

# Logical check with the input
is_adult = age >= 18
print(f"Is Adult (18+): {is_adult}")