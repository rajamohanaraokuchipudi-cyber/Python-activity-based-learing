# Assignment 14: Warehouse Inventory Reconciliation
products = int(input("Enter number of products: "))

for i in range(products):
    print(f"\nProduct {i + 1}")
    name = input("Product name: ")
    opening = int(input("Opening stock: "))
    incoming = int(input("Incoming quantity: "))
    dispatched = int(input("Dispatched quantity: "))
    actual = int(input("Actual closing stock: "))

    expected = opening + incoming - dispatched
    difference = actual - expected
    print("Expected closing stock:", expected)
    print("Actual closing stock:", actual)
    if difference == 0:
        print("Status: Stock matches.")
    elif difference < 0:
        print("Status: Stock shortage of", abs(difference))
    else:
        print("Status: Stock surplus of", difference)

    target = int(input("Desired stock level: "))
    replenishment = max(0, target - actual)
    print("Replenishment required:", replenishment)
