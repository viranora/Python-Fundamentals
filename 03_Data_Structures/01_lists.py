"""
Python Fundamentals - 07 Lists (Data Structures)
Description: Lists are ordered, mutable collections. 
This file covers creating, accessing, modifying, and slicing lists.
"""

# ==========================================
# 1. Creating and Accessing Lists
# ==========================================
# Lists are defined with square brackets []
# Indexing starts at 0.

# A list of string elements
programming_languages = ["Python", "Java", "C++", "JavaScript", "Go"]

print("--- Accessing Elements ---")
print("Original List:", programming_languages)
print("First Element [0]:", programming_languages[0])   # Python
print("Third Element [2]:", programming_languages[2])   # C++
print("Last Element [-1]:", programming_languages[-1])  # Go (Negative indexing starts from end)


# ==========================================
# 2. Slicing Lists (Getting a part of it)
# ==========================================
# Syntax: list[start : stop : step]
# 'stop' index is NOT included!

print("\n--- Slicing ---")
print("First 3 items [0:3]:", programming_languages[0:3]) # 0, 1, 2
print("Items from index 2 to end [2:]:", programming_languages[2:])


# ==========================================
# 3. Modifying Lists (Mutable)
# ==========================================
# Unlike Strings, Lists can be changed after creation.

print("\n--- Modifying ---")
programming_languages[1] = "C#"  # Changing 'Java' to 'C#'
print("After Update:", programming_languages)

# Adding items
programming_languages.append("Rust") # Adds to the end
print("After Append:", programming_languages)

programming_languages.insert(0, "Swift") # Inserts at specific index (0)
print("After Insert at [0]:", programming_languages)


# ==========================================
# 4. Removing Items
# ==========================================

print("\n--- Removing ---")
programming_languages.remove("C++") # Remove by value
print("After Removing 'C++':", programming_languages)

last_item = programming_languages.pop() # Removes the last item and returns it
print(f"Popped Item: {last_item}")
print("Final List:", programming_languages)


# ==========================================
# 5. Sorting and Length
# ==========================================

print("\n--- Utility Methods ---")
print("Length of list:", len(programming_languages))

programming_languages.sort() # Sorts alphabetically (A-Z) permanently
print("Sorted List:", programming_languages)