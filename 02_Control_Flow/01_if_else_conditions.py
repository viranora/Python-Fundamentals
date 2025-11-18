"""
Python Fundamentals - 04 If / Else Conditions
Description: This file demonstrates decision-making logic using if, elif, and else.
It implements a simple Student Grading System.
"""

# ==========================================
# 1. Simple If / Else
# ==========================================

user_input = input("Enter your exam score (0-100): ")
score = int(user_input)

# Basic Validation Logic
if score < 0 or score > 100:
    print("Error: Please enter a valid score between 0 and 100.")
else:
    print(f"Valid score received: {score}")

    # ==========================================
    # 2. Elif (Else If) Ladder
    # ==========================================
    # Python checks conditions from top to bottom.
    # Once a condition is met, it skips the rest.
    
    # Note the indentation here! We are inside the 'else' block above.
    if score >= 90:
        grade = "AA"
        status = "Excellent"
    elif score >= 85:
        grade = "BA"
        status = "Very Good"
    elif score >= 70:
        grade = "BB"
        status = "Good"
    elif score >= 50:
        grade = "CC"
        status = "Passed"
    else:
        grade = "FF"
        status = "Failed"

    print(f"--- Result ---")
    print(f"Grade: {grade}")
    print(f"Status: {status}")


# ==========================================
# 3. Nested If (If inside If)
# ==========================================
# Example: Scholarship check
# You need high grade AND financial need.

is_scholarship_student = True

if grade == "AA":
    if is_scholarship_student:
        print("\n[System]: You qualify for the Honor Scholarship!")
    else:
        print("\n[System]: Congratulations on the high score!")