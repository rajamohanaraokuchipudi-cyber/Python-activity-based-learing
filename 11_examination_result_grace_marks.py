# Assignment 11: Examination Result and Grace-Mark Validation
subjects = int(input("Enter number of subjects: "))
max_marks = int(input("Enter maximum marks per subject: "))
pass_mark = int(input("Enter pass mark per subject: "))
grace_limit = int(input("Enter maximum grace marks allowed per subject: "))

marks = []
for i in range(subjects):
    mark = int(input(f"Enter marks for subject {i + 1}: "))
    if mark < 0 or mark > max_marks:
        print("Invalid marks entered.")
        raise SystemExit
    if mark < pass_mark and pass_mark - mark <= grace_limit:
        print(f"Subject {i + 1}: Grace marks applied.")
        mark = pass_mark
    marks.append(mark)

total = sum(marks)
percentage = total / (subjects * max_marks) * 100
failed = [i + 1 for i, mark in enumerate(marks) if mark < pass_mark]

print("\nFinal Marks:", marks)
print("Total:", total)
print(f"Percentage: {percentage:.2f}%")
if failed:
    print("Result: Fail")
    print("Failed subjects:", failed)
else:
    print("Result: Pass")
    if percentage >= 75:
        print("Classification: Distinction")
    elif percentage >= 60:
        print("Classification: First Class")
    elif percentage >= 50:
        print("Classification: Second Class")
    else:
        print("Classification: Pass Class")
