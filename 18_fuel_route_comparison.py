# Assignment 18: Fuel Consumption and Route Comparison
vehicles = int(input("Number of vehicle options: "))
distance = float(input("Journey distance in km: "))
reserve_percent = float(input("Required fuel reserve percentage: "))

options = []
for i in range(vehicles):
    print(f"\nVehicle {i + 1}")
    name = input("Vehicle name: ")
    mileage = float(input("Mileage (km per litre): "))
    price = float(input("Fuel price per litre: "))
    available = float(input("Fuel currently available (litres): "))

    if mileage <= 0 or price < 0 or available < 0:
        print("Invalid vehicle data; skipped.")
        continue

    needed = distance / mileage
    total_needed = needed * (1 + reserve_percent / 100)
    cost = needed * price
    feasible = available >= total_needed
    options.append((name, needed, total_needed, cost, feasible))
    print(f"Fuel for journey: {needed:.2f} L")
    print(f"Fuel including reserve: {total_needed:.2f} L")
    print(f"Estimated journey cost: Rs. {cost:.2f}")
    print("Feasible:", "Yes" if feasible else "No")

feasible_options = [v for v in options if v[4]]
if feasible_options:
    best = min(feasible_options, key=lambda v: v[3])
    print("\nLowest-cost feasible option:", best[0], f"(Rs. {best[3]:.2f})")
else:
    print("\nNo vehicle has enough fuel for the journey and reserve.")
