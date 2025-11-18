"""
Python Fundamentals - 15 Encapsulation
Author: [Your Name]
Description: 
- Encapsulation: Hiding data to prevent unauthorized access/modification.
- Public Members: Accessible from anywhere.
- Protected Members (_): Should not be accessed directly (Convention).
- Private Members (__): Cannot be accessed directly (Enforced).
- Getters & Setters: Methods to access private data safely.
"""

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner       # Public: Everyone can see/change
        self._currency = "USD"   # Protected: Suggests "Don't touch", but allows it.
        self.__balance = balance # Private: Strictly hidden!

    # ==========================================
    # Getters (Read Only Access)
    # ==========================================
    def get_balance(self):
        # We can add security checks here (e.g., log who is looking)
        return self.__balance

    # ==========================================
    # Setters (Write Access with Validation)
    # ==========================================
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New Balance: ${self.__balance}")
        else:
            print("Error: Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New Balance: ${self.__balance}")
        else:
            print("Error: Insufficient funds or invalid amount.")

# ==========================================
# Testing Encapsulation
# ==========================================

account = BankAccount("Sema", 1000)

print("--- Public Access ---")
print("Owner:", account.owner) # Works fine

print("\n--- Controlled Access (Getters/Setters) ---")
account.deposit(500)    # Works: Logic allows it
account.withdraw(2000)  # Fails: Logic prevents it (Balance protection)
print("Current Balance:", account.get_balance())

print("\n--- Direct Access Attempts (Hacking) ---")

# 1. Accessing Protected Variable (Not recommended but possible)
print("Currency (_):", account._currency) 

# 2. Accessing Private Variable (Will Crash!)
try:
    print("Balance (__):", account.__balance)
except AttributeError as e:
    print(f"FAILED! Python says: {e}")
    print(">> You cannot touch the private variable directly!")

# Even if you try to force set it:
account.__balance = 9999999 # This actually creates a NEW dummy variable, doesn't change the real one.
print("Real Balance via Getter:", account.get_balance()) # Still the original secure balance