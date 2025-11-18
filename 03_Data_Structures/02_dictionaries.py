"""
Python Fundamentals - 08 Dictionaries
Description: Dictionaries store data in Key-Value pairs.
They are optimized for fast data retrieval (Hash Map logic).
"""

# ==========================================
# 1. Creating a Dictionary
# ==========================================
# Syntax: {key: value, key: value}
# Keys must be unique and immutable (strings, numbers).

student = {
    "name": "Sema",
    "age": 22,
    "department": "Computer Engineering",
    "gpa": 3.45,
    "is_graduated": False
}

print("--- Accessing Data ---")
# Access values by referring to the Key name
print("Student Name:", student["name"])
print("Department:", student["department"])

# Safe access using .get() (Prevents error if key doesn't exist)
print("Scholarship Status:", student.get("scholarship", "Not Found")) 


# ==========================================
# 2. Modifying Dictionaries
# ==========================================

print("\n--- Modifying ---")
student["gpa"] = 3.80        # Update existing value
student["internship"] = "AI Company" # Add new key-value pair
print("Updated Student:", student)

# Removing items
del student["is_graduated"]
print("After Deletion:", student)


# ==========================================
# 3. Dictionary Methods (Looping)
# ==========================================

print("\n--- Looping through Dictionary ---")
# .keys() -> Returns list of keys
# .values() -> Returns list of values
# .items() -> Returns list of tuples (key, value)

for key, value in student.items():
    print(f"{key}: {value}")


# ==========================================
# 4. Nested Dictionaries (JSON Structure)
# ==========================================
# Real-world data often looks like this (e.g., from an API).

classroom = {
    "student_1": {
        "name": "Sema",
        "grades": [90, 85, 92]
    },
    "student_2": {
        "name": "Ali",
        "grades": [70, 60, 75]
    }
}

print("\n--- Nested Dictionary ---")
# Accessing deep data: Get student_1's second grade
print("Sema's 2nd Grade:", classroom["student_1"]["grades"][1])