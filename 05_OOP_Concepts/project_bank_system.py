"""
Python Fundamentals - Final Project: Bank Management System
Description: 
A comprehensive OOP example simulating a banking system.
- BankAccount: Base class with encapsulation.
- SavingsAccount: Child class with interest rate calculation.
- CheckingAccount: Child class with overdraft (credit) limit.
"""

# ==========================================
# 1. The Base Class (Parent)
# ==========================================
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.__balance = balance  # Private attribute (Encapsulation)
    
    def deposit(self, amount):
        """Adds money to the account safely."""
        if amount > 0:
            self.__balance += amount
            print(f"[Success] {self.account_holder} deposited ${amount}. New Balance: ${self.__balance}")
        else:
            print("[Error] Deposit amount must be positive.")

    def withdraw(self, amount):
        """Basic withdraw logic. Validates funds."""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"[Success] {self.account_holder} withdrew ${amount}. Remaining: ${self.__balance}")
        else:
            print(f"[Error] Insufficient funds! Balance: ${self.__balance}")

    def get_balance(self):
        """Getter for private balance attribute."""
        return self.__balance

    def display_info(self):
        print(f"User: {self.account_holder} | Balance: ${self.__balance}")


# ==========================================
# 2. Child Class: Savings Account (Vadeli Hesap)
# ==========================================
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance, interest_rate=0.05):
        super().__init__(account_holder, balance) # Call Parent's __init__
        self.interest_rate = interest_rate

    def apply_interest(self):
        """Calculates and adds interest to the balance."""
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest) # We reuse the Parent's deposit method!
        print(f"-> Interest applied (${interest}) at rate {self.interest_rate*100}%")


# ==========================================
# 3. Child Class: Checking Account (Vadesiz/Kredili Hesap)
# ==========================================
class CheckingAccount(BankAccount):
    def __init__(self, account_holder, balance, overdraft_limit=500):
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit

    # METHOD OVERRIDING (Polymorphism)
    # We change the logic of withdraw solely for this class.
    def withdraw(self, amount):
        available_funds = self.get_balance() + self.overdraft_limit
        
        if 0 < amount <= available_funds:
            new_balance = self.get_balance() - amount
            # We need to hack the private variable a bit via a protected method or logic,
            # but here we will just simulate the logic since __balance is private.
            # NOTE: In a real system, Parent would have a protected _set_balance method.
            
            # Workaround for demo: Withdraw all balance first, then track debt if needed.
            # Or better: Since we cannot access __balance directly to set it negative,
            # we use the Parent's withdraw for the covered part.
            
            if amount <= self.get_balance():
                super().withdraw(amount)
            else:
                # Using Overdraft
                diff = amount - self.get_balance()
                super().withdraw(self.get_balance()) # Empty the account
                print(f"[Overdraft Used] You are now in debt by ${diff} (Limit: ${self.overdraft_limit})")
        else:
            print(f"[Error] Overdraft limit exceeded! Max withdrawable: ${available_funds}")


# ==========================================
# 4. Main Simulation
# ==========================================
if __name__ == "__main__":
    print("=== BANK SYSTEM SIMULATION ===\n")

    # 1. Standard Savings Account
    print("--- Scenario 1: Savings Account ---")
    sa = SavingsAccount("Sema", 1000)
    sa.deposit(500)
    sa.apply_interest() # Adds 5%
    sa.display_info()

    print("\n--- Scenario 2: Checking Account (Overdraft) ---")
    # 2. Checking Account with Credit Limit
    ca = CheckingAccount("Ali", 100)
    ca.withdraw(50)  # Normal withdraw
    ca.withdraw(300) # Uses Overdraft (Balance 50 + Limit 500 = 550 available)
    ca.withdraw(1000) # Fails (Exceeds limit)