"""
Python Fundamentals - 16 File Writing
Description: 
- Creates and writes data to a text file.
- Modes: 'w' (Write - Overwrites), 'a' (Append - Adds to end).
- context manager 'with open()' ensures file is closed automatically.
"""

# ==========================================
# 1. Writing to a File ('w' Mode)
# ==========================================
# If file doesn't exist, it creates it.
# If it exists, it WIPES everything and writes new.

print("--- Writing to File ---")
filename = "dev_logs.txt"

with open(filename, "w", encoding="utf-8") as file:
    file.write("Log Entry 1: System Started.\n")
    file.write("Log Entry 2: User Sema logged in.\n")
    file.write("Log Entry 3: Database connected.\n")

print(f"Successfully wrote to {filename}.")


# ==========================================
# 2. Appending to a File ('a' Mode)
# ==========================================
# Adds content to the end without deleting old data.
# Ideal for logging systems.

print("\n--- Appending to File ---")

with open(filename, "a", encoding="utf-8") as file:
    file.write("Log Entry 4: Warning - High Memory Usage.\n")
    file.write("Log Entry 5: System Shutdown.\n")

print("New logs appended.")