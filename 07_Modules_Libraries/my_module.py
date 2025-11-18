"""
My Custom Utility Module
Description: Contains reusable math and string functions.
This file is NOT meant to be run directly, but imported.
"""

def calculate_tax(price, tax_rate=0.18):
    """Calculates price with tax."""
    return price * (1 + tax_rate)

def format_username(name):
    """Cleans and formats a username."""
    return name.strip().lower().replace(" ", "_")

# This block only runs if you run THIS file directly.
# If imported, this part is ignored.
if __name__ == "__main__":
    print("Debug Mode: Testing functions...")
    print(format_username("  Sema Nur  ")) # sema_nur