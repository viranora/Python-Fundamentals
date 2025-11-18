"""
Python Fundamentals - 11 *Args and **Kwargs
Description: Handling flexible number of arguments in functions.
- *args: Collects extra positional arguments into a TUPLE.
- **kwargs: Collects extra keyword arguments into a DICTIONARY.
"""

# ==========================================
# 1. *ARGS (Variable Positional Arguments)
# ==========================================
# Allows passing ANY number of arguments.
# Inside the function, 'numbers' becomes a TUPLE.

def sum_all(*numbers):
    """Calculates the sum of all given numbers."""
    print(f"Debug: Type of args: {type(numbers)} | Content: {numbers}")
    
    total = 0
    for num in numbers:
        total += num
    return total

print("--- *Args Example ---")
result1 = sum_all(10, 20)
print("Sum (2 items):", result1)

result2 = sum_all(1, 2, 3, 4, 5, 100) # Can pass as many as we want
print("Sum (6 items):", result2)


# ==========================================
# 2. **KWARGS (Variable Keyword Arguments)
# ==========================================
# Allows passing ANY number of KEY=VALUE arguments.
# Inside the function, 'info' becomes a DICTIONARY.

def build_profile(**info):
    """Creates a user profile dynamically."""
    print(f"\nDebug: Type of kwargs: {type(info)} | Content: {info}")
    
    # We can access data just like a dictionary
    for key, value in info.items():
        print(f"- {key}: {value}")

print("\n--- **Kwargs Example ---")
# We can send different data for different users without changing the function
build_profile(name="Sema", age=22, role="Engineer")
build_profile(name="Ali", city="Istanbul", language="Python", level="Expert")


# ==========================================
# 3. Combined Usage
# ==========================================
# Order matters: 1. Standard, 2. *args, 3. **kwargs

def super_function(required_arg, *args, **kwargs):
    print(f"\nRequired: {required_arg}")
    print(f"Args (Tuple): {args}")
    print(f"Kwargs (Dict): {kwargs}")

print("\n--- Combined Example ---")
super_function("Hello", 1, 2, 3, color="Blue", mode="Dark")