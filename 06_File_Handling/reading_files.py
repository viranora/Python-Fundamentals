"""
Python Fundamentals - 17 File Reading
Author: [Your Name]
Description: Reading data from text files safely using try-except blocks.
"""

filename = "dev_logs.txt"

print(f"--- Reading from {filename} ---")

try:
    with open(filename, "r", encoding="utf-8") as file:
        # Method 1: Read line by line (Best for memory)
        for line in file:
            print(f"Read: {line.strip()}") # .strip() removes the newline character (\n)

        # Method 2: Read all lines into a list (Good for small files)
        # file.seek(0) # Move cursor back to top if you want to read again
        # content_list = file.readlines()
        # print(content_list)

except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found. Please run writing_files.py first.")
except Exception as e:
    print(f"An error occurred: {e}")