# Assignment 16: Multi-Day Water Tank Simulation
capacity = float(input("Tank capacity in litres: "))
level = float(input("Starting water level in litres: "))
threshold = float(input("Target threshold in litres: "))
days = int(input("Number of intervals/days: "))

if capacity <= 0 or not 0 <= level <= capacity or not 0 <= threshold <= capacity:
    print("Invalid tank details.")
    raise SystemExit

first_threshold = None
for day in range(1, days + 1):
    inflow = float(input(f"Day {day} inflow (litres): "))
    outflow = float(input(f"Day {day} outflow (litres): "))
    level += inflow - outflow

    if level > capacity:
        print(f"Day {day}: Overflow of {level - capacity:.2f} litres.")
        level = capacity
    elif level < 0:
        print(f"Day {day}: Shortage of {-level:.2f} litres.")
        level = 0

    print(f"Water level after day {day}: {level:.2f} litres")
    if first_threshold is None and level >= threshold:
        first_threshold = day

if first_threshold is None:
    print("Threshold was not reached.")
else:
    print("First interval reaching threshold:", first_threshold)
