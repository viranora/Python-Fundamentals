"""
Python Fundamentals - 18 Modules & Imports
Author: [Your Name]
Description: Demonstrates how to import custom modules and built-in libraries.
"""

# 1. Importing Built-in Python Libraries
import math
import datetime

# 2. Importing YOUR Custom Module
# Note: my_module.py must be in the same folder or python path.
import my_module as tools  # Using an alias 'tools'

# ==========================================
# Using Built-in Libraries
# ==========================================
print("--- Built-in Modules ---")
print(f"Square root of 16: {math.sqrt(16)}")

today = datetime.date.today()
print(f"Today's Date: {today}")


# ==========================================
# Using Custom Module
# ==========================================
print("\n--- Custom Module Usage ---")

product_price = 1000
final_price = tools.calculate_tax(product_price)
print(f"Price with Tax: ${final_price}")

raw_user = "  Sema Nur Ozyilmaz  "
clean_user = tools.format_username(raw_user)
print(f"Formatted Username: {clean_user}")