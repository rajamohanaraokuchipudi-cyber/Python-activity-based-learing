# Assignment 15: Smart Parking Fee Management
from datetime import datetime

entry_text = input("Entry time (YYYY-MM-DD HH:MM): ")
exit_text = input("Exit time (YYYY-MM-DD HH:MM): ")
vehicle = input("Vehicle category (bike/car): ").strip().lower()
hourly_rate = {"bike": 20, "car": 50}

try:
    entry = datetime.strptime(entry_text, "%Y-%m-%d %H:%M")
    exit_time = datetime.strptime(exit_text, "%Y-%m-%d %H:%M")
except ValueError:
    print("Invalid date/time format.")
    raise SystemExit

if exit_time <= entry:
    print("Invalid time: exit must be after entry.")
elif vehicle not in hourly_rate:
    print("Invalid vehicle category.")
else:
    minutes = int((exit_time - entry).total_seconds() // 60)
    hours = (minutes + 59) // 60
    days = minutes // (24 * 60)
    fee = hours * hourly_rate[vehicle]
    daily_limit = 200 if vehicle == "bike" else 500
    fee = min(fee, (days + 1) * daily_limit)
    if days > 0:
        print("Overnight parking: Yes")
    else:
        print("Overnight parking: No")
    print("Parking duration:", hours, "hour(s)")
    print("Parking fee: Rs.", fee)
