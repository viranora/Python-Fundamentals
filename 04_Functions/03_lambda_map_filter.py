"""
Python Fundamentals - 12 Lambda, Map, and Filter
Description: 
- Lambda: Anonymous, one-line functions.
- Map: Applies a function to every item in a list.
- Filter: Selects items from a list based on a condition.
"""

# ==========================================
# 1. LAMBDA FUNCTIONS (Anonymous Functions)
# ==========================================
# Syntax: lambda arguments : expression
# Traditional way vs Lambda way

# Traditional
def square_traditional(x):
    return x * x

# Lambda (One-liner)
square_lambda = lambda x: x * x

print("--- Lambda Basics ---")
print("Traditional(5):", square_traditional(5))
print("Lambda(5):", square_lambda(5))

# Multi-argument lambda
multiply = lambda a, b: a * b
print("Lambda Multiply(3, 4):", multiply(3, 4))


# ==========================================
# 2. MAP FUNCTION (Transform Data)
# ==========================================
# Logic: map(function, list) -> Applies function to ALL items.
# Very common in Data Science (e.g., converting units).

prices_usd = [10, 20, 50, 100]
exchange_rate = 34.5

# Using Lambda inside Map
# We convert the map object to a list to see the result.
prices_try = list(map(lambda p: p * exchange_rate, prices_usd))

print("\n--- Map Function ---")
print("Original (USD):", prices_usd)
print("Converted (TRY):", prices_try)


# ==========================================
# 3. FILTER FUNCTION (Select Data)
# ==========================================
# Logic: filter(function, list) -> Returns only items where function is True.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter only even numbers (x % 2 == 0)
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("\n--- Filter Function ---")
print("All Numbers:", numbers)
print("Even Numbers:", even_numbers)


# ==========================================
# 4. Real World Example (Data Cleaning)
# ==========================================
emails = ["sema@gmail.com", "user@yahoo.com", "admin@gmail.com", "test@hotmail.com"]

# Goal: Get only 'gmail' users
gmail_users = list(filter(lambda email: "gmail.com" in email, emails))

print("\n--- Data Cleaning Example ---")
print("Gmail Users:", gmail_users)