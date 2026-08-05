# Student Result & Scholarship Eligibility System

# 1. Take student information as input
name = input("Enter student's name: ")
age = int(input("Enter student's age: "))
mark1 = int(input("Enter marks for Subject 1: "))
mark2 = int(input("Enter marks for Subject 2: "))
mark3 = int(input("Enter marks for Subject 3: "))

# 2. Calculate total and average
total = mark1 + mark2 + mark3
average = total / 3

# 3. Assign grade using if-elif-else
if average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

# 4. Determine pass/fail using logical operators
# Student must have average >= 50 AND no subject below 40 to pass
if average >= 50 and mark1 >= 40 and mark2 >= 40 and mark3 >= 40:
    result = "PASS"
else:
    result = "FAIL"

# 5. Determine scholarship eligibility
# Eligible if average >= 75 AND age <= 25
if average >= 75 and age <= 25:
    scholarship = True
else:
    scholarship = False

# 6. Calculate final tuition fee after discount
base_fee = 10000

if scholarship:
    discount = base_fee * 0.20   # 20% discount
else:
    discount = 0

final_fee = base_fee - discount

# Display Results
print("\n----- STUDENT RESULT SUMMARY -----")
print("Name:", name)
print("Age:", age)
print("Total Marks:", total)
print("Average Marks:", average)
print("Grade:", grade)
print("Result:", result)

if scholarship:
    print("Scholarship: Eligible")
else:
    print("Scholarship: Not Eligible")

print("Base Tuition Fee:", base_fee)
print("Discount:", discount)
print("Final Tuition Fee to Pay:", final_fee)