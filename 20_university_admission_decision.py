# Assignment 20: University Admission Decision Engine
candidates = int(input("Number of candidates: "))
required_subject_mark = float(input("Minimum mark in required subject: "))
minimum_aggregate = float(input("Minimum aggregate percentage: "))
course_threshold = float(input("Course-specific entrance score threshold: "))

eligible = []
for i in range(candidates):
    print(f"\nCandidate {i + 1}")
    name = input("Name: ")
    subject_mark = float(input("Required subject mark: "))
    aggregate = float(input("Aggregate percentage: "))
    entrance = float(input("Course entrance score: "))

    if (subject_mark >= required_subject_mark and
            aggregate >= minimum_aggregate and
            entrance >= course_threshold):
        eligible.append((name, aggregate, entrance))
        print("Status: Eligible")
    else:
        print("Status: Not eligible")

# Rank by aggregate first, then entrance score, both highest first.
eligible.sort(key=lambda candidate: (candidate[1], candidate[2]), reverse=True)

print("\nRanked Eligible Candidates")
if not eligible:
    print("No eligible candidates.")
else:
    for rank, candidate in enumerate(eligible, start=1):
        print(f"{rank}. {candidate[0]} | Aggregate: {candidate[1]:.2f}% | "
              f"Entrance score: {candidate[2]:.2f}")
