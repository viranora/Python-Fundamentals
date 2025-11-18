"""
Python Fundamentals - 06 While Loops
Description: This file demonstrates the 'while' loop, which runs as long as
a condition is True. It creates a simple interactive menu system.
"""

# ==========================================
# 1. Basic While Loop
# ==========================================
# Warning: If the condition never becomes False, you get an INFINITE LOOP!
# To stop an infinite loop in terminal, press 'Ctrl + C'.

count = 1
print("--- Countdown ---")
while count <= 5:
    print(f"Count: {count}")
    count += 1  # CRITICAL: We must update the variable to eventually stop the loop.


# ==========================================
# 2. Interactive Menu (Real World Use Case)
# ==========================================
# Most apps run inside a while loop waiting for user input.

print("\n--- System Menu ---")
user_command = ""

# The loop continues until the user types 'quit'
while user_command != "quit":
    user_command = input("Enter command (start/help/quit): ").lower() # .lower() converts input to lowercase
    
    if user_command == "start":
        print(">> System starting...")
    elif user_command == "help":
        print(">> Support: Contact admin@example.com")
    elif user_command == "quit":
        print(">> Exiting system. Goodbye!")
    else:
        print(">> Unknown command. Please try again.")

print("Program has finished.")