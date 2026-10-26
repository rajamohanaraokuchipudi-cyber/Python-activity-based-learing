# Assignment 12: Attendance Recovery Computation
attended = int(input("Classes attended so far: "))
conducted = int(input("Total classes conducted so far: "))
target = float(input("Required attendance percentage: "))

if conducted <= 0 or attended < 0 or attended > conducted or not 0 < target <= 100:
    print("Invalid input.")
else:
    current = attended / conducted * 100
    print(f"Current attendance: {current:.2f}%")
    if current >= target:
        print("You already meet the attendance requirement.")
    else:
        # Assumes every future class is attended.
        needed = 0
        while (attended + needed) / (conducted + needed) * 100 < target:
            needed += 1
        print("Minimum consecutive classes to attend:", needed)

        # Scenario where 1 in every 5 future classes is missed
        attended_future = 0
        total_future = 0
        while (attended + attended_future) / (conducted + total_future) * 100 < target:
            total_future += 1
            if total_future % 5 != 0:
                attended_future += 1
        print("Classes needed if one out of every five future classes is missed:",
              total_future)
