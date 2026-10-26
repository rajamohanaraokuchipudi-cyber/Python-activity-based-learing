# Assignment 17: Student Performance Trend Analysis
students = int(input("Number of students: "))
subjects = int(input("Number of subjects: "))
assessments = int(input("Number of assessments per subject: "))

for s in range(students):
    name = input(f"\nStudent {s + 1} name: ")
    weak_subjects = []
    total_change = 0

    for sub in range(subjects):
        subject = input("Subject name: ")
        scores = []
        for a in range(assessments):
            scores.append(float(input(f"  Assessment {a + 1} score: ")))
        change = scores[-1] - scores[0]
        total_change += change
        average = sum(scores) / len(scores)
        print(f"{subject}: average={average:.2f}, change={change:.2f}")
        if average < 50:
            weak_subjects.append(subject)

    print("Student:", name)
    print(f"Overall trend score (sum of subject changes): {total_change:.2f}")
    print("Consistently weak subjects:", weak_subjects if weak_subjects else "None")
    if total_change > 0:
        print("Trend: Improving")
    elif total_change < 0:
        print("Trend: Declining")
    else:
        print("Trend: No overall change")
