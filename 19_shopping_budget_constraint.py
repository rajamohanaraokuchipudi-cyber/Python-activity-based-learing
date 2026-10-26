# Assignment 19: Multi-Product Shopping Budget Constraint
budget = float(input("Enter shopping budget: "))
count = int(input("Number of products: "))
basket = []

for i in range(count):
    name = input(f"Product {i + 1} name: ")
    price = float(input("Price per unit: "))
    quantity = int(input("Quantity: "))
    if price < 0 or quantity < 0:
        print("Invalid item; using zero quantity.")
        quantity = 0
    basket.append([name, price, quantity])

def total_cost(items):
    return sum(price * qty for _, price, qty in items)

subtotal = total_cost(basket)
discount = subtotal * 0.10 if subtotal >= 5000 else 0
final_total = subtotal - discount
print(f"Subtotal: Rs. {subtotal:.2f}")
print(f"Discount: Rs. {discount:.2f}")
print(f"Final total: Rs. {final_total:.2f}")

# Reduce quantities from the most expensive items until within budget.
basket.sort(key=lambda item: item[1], reverse=True)
while total_cost(basket) - (total_cost(basket) * 0.10 if total_cost(basket) >= 5000 else 0) > budget:
    changed = False
    for item in basket:
        if item[2] > 0:
            item[2] -= 1
            changed = True
            break
    if not changed:
        break

reduced_subtotal = total_cost(basket)
reduced_discount = reduced_subtotal * 0.10 if reduced_subtotal >= 5000 else 0
print("\nAdjusted basket to fit budget:")
for name, price, qty in basket:
    print(f"{name}: {qty} unit(s)")
print(f"Adjusted final total: Rs. {reduced_subtotal - reduced_discount:.2f}")
