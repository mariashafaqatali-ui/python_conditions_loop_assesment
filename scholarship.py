# Topic 1: Conditional Statements
# Task 1: Student Scholarship Eligibility System
# Topic: if, elif, else, comparison operators, and logical thinking.

# Real-World Scenario
# A university gives scholarships to students based on their academic
# marks, attendance percentage, and monthly family income.
# The university follows these rules:
# - Academic marks must be at least 80%.
# - Attendance must be at least 85%.
# - Monthly family income must be Rs. 50,000 or less.
# - If all conditions are satisfied:
#   - Marks of 90% or above: Full Scholarship.
#   - Marks between 80% and 89%: Partial Scholarship.
# - If any condition is not satisfied, the program must display
#   the reason for ineligibility.
# - The program must display a complete scholarship evaluation report.

print("===== SCHOLARSHIP ELIGIBILITY SYSTEM =====")

name = "Maria"
print(f"Student Name: {name}")
marks = float(input("Enter academic marks (%): "))
attendance = float(input("Enter attendance percentage (%): "))
income = float(input("Enter monthly family income (Rs.): "))

if marks < 0 or marks > 100:
    print("\nInvalid input: Marks must be between 0 and 100.")
elif attendance < 0 or attendance > 100:
    print("\nInvalid input: Attendance must be between 0 and 100.")
elif income < 0:
    print("\nInvalid input: Income cannot be negative.")
else:
    if marks < 80:
        status = "Not Eligible"
        scholarship = "None"
        reason = "Academic marks are less than 80%."
    elif attendance < 85:
        status = "Not Eligible"
        scholarship = "None"
        reason = "Attendance is less than 85%."
    elif income > 50000:
        status = "Not Eligible"
        scholarship = "None"
        reason = "Monthly family income is more than Rs. 50,000."
    elif marks >= 90:
        status = "Eligible"
        scholarship = "Full Scholarship"
        reason = "All conditions are satisfied."
    else:
        status = "Eligible"
        scholarship = "Partial Scholarship"
        reason = "All conditions are satisfied."

    print("\n===== SCHOLARSHIP EVALUATION REPORT =====")
    print(f"Student Name: {name}")
    print(f"Academic Marks: {marks:.2f}%")
    print(f"Attendance: {attendance:.2f}%")
    print(f"Monthly Family Income: Rs. {income:.2f}")
    print(f"Eligibility Status: {status}")
    print(f"Scholarship Type: {scholarship}")
    print(f"Reason: {reason}")

    if status == "Eligible":
        print(f"Congratulations {name}! You received a {scholarship}.")