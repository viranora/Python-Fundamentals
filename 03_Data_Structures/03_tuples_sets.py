"""
Python Fundamentals - 09 Tuples & Sets
Description: 
- Tuples: Immutable (unchangeable) ordered collections.
- Sets: Unordered collections of UNIQUE elements (Mathematical sets).
"""

# ==========================================
# 1. TUPLES (Immutable Lists)
# ==========================================
# Defined with parentheses ()
# Faster than lists because they are static.

coordinates = (41.0082, 28.9784) # Latitude, Longitude (Istanbul)

print("--- Tuples ---")
print("Coordinates:", coordinates)
print("Latitude:", coordinates[0])

# IMMUTABILITY CHECK:
# The following line would cause a TypeError because tuples cannot be changed.
# coordinates[0] = 42.0  <-- This will crash the program if uncommented.


# Tuple Unpacking (Very Pythonic!)
# Assigning tuple values to variables in one line.
lat, lng = coordinates
print(f"Unpacked -> Lat: {lat}, Lng: {lng}")


# ==========================================
# 2. SETS (Unique Collections)
# ==========================================
# Defined with curly brackets {} like dictionaries, but without keys.
# Automatically removes duplicates!

id_numbers = {101, 102, 103, 101, 102} # Duplicate 101 and 102

print("\n--- Sets ---")
print("Original Set (Duplicates removed):", id_numbers) 
# Output will only show {101, 102, 103}

# Adding/Removing
id_numbers.add(104)
id_numbers.remove(101)
print("Updated Set:", id_numbers)


# ==========================================
# 3. Set Operations (Math Logic)
# ==========================================
# Powerful for finding common or different items between two groups.

class_A = {"Ali", "Ayse", "Mehmet"}
class_B = {"Ayse", "Fatma", "Mehmet"}

print("\n--- Set Math ---")
# Intersection (Ortak Elemanlar): Who is in BOTH classes?
common_students = class_A.intersection(class_B)
print("Intersection (A & B):", common_students)

# Difference (Fark): Who is in A but NOT in B?
diff_students = class_A.difference(class_B)
print("Difference (A - B):", diff_students)

# Union (Birleşim): All unique students from both classes
all_students = class_A.union(class_B)
print("Union (A | B):", all_students)