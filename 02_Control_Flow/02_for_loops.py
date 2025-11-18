"""
Python Fundamentals - 05 For Loops
Description: This file demonstrates the 'for' loop structure, the range() function,
and loop control statements (break/continue).
"""

# ==========================================
# 1. The range() Function
# ==========================================
# range(start, stop, step) generates a sequence of numbers.
# Note: 'stop' is exclusive (it goes up to, but does not include the stop number).

print("--- Counting from 1 to 5 ---")
for i in range(1, 6): # Generates: 1, 2, 3, 4, 5
    print(f"Iteration: {i}")

print("\n--- Even Numbers (Step example) ---")
for i in range(0, 11, 2): # Start at 0, go to 10, increase by 2
    print(f"Even Number: {i}")


# ==========================================
# 2. Iterating Over a Sequence (List)
# ==========================================
# For loops are perfect for going through items in a list (e.g., processing data).

technologies = ["Python", "Java", "C++", "React", "SQL"]

print("\n--- My Tech Stack ---")
for tech in technologies:
    print(f"I am learning: {tech}")


# ==========================================
# 3. Loop Control: Break & Continue
# ==========================================
# break: Stops the loop completely.
# continue: Skips the current step and jumps to the next one.

print("\n--- Search Mechanism (Break) ---")
target = "C++"

for tech in technologies:
    if tech == target:
        print(f"Found {target}! Stopping the loop.")
        break  # Exits the loop immediately
    print(f"Checking... {tech}")


print("\n--- Filter Mechanism (Continue) ---")
# Let's print only programming languages (skip SQL for this example)

for tech in technologies:
    if tech == "SQL":
        continue  # Skips the rest of the code for SQL, goes to next item
    print(f"Programming Language: {tech}")