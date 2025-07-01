subjects = ["English", "Maths", "Science", "History", "Computer"]

marks = []

print("Enter marks for the following subjects:")

for subject in subjects:
    m = float(input(f"{subject}: "))
    marks.append(m)

total = sum(marks)
percentage = total / len(subjects)

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("\n--- Student Summary ---")
for i in range(len(subjects)):
    print(f"{subjects[i]}: {marks[i]}")

print("Total Marks:", total)
print("Percentage:", round(percentage, 2))
print("Grade:", grade)
