# Assignment 13: ATM Transaction Sequence Simulation
balance = float(input("Enter opening balance: "))
withdrawal_limit = float(input("Maximum allowed withdrawal per transaction: "))
transactions = []

count = int(input("How many transactions? "))
for i in range(count):
    kind = input(f"Transaction {i + 1} (deposit/withdraw): ").strip().lower()
    amount = float(input("Amount: "))

    if amount <= 0:
        print("Rejected: amount must be positive.")
        transactions.append((kind, amount, "Rejected"))
    elif kind == "deposit":
        balance += amount
        transactions.append((kind, amount, "Accepted"))
    elif kind == "withdraw":
        if amount > withdrawal_limit:
            print("Rejected: exceeds withdrawal limit.")
            transactions.append((kind, amount, "Rejected"))
        elif amount > balance:
            print("Rejected: insufficient balance.")
            transactions.append((kind, amount, "Rejected"))
        else:
            balance -= amount
            transactions.append((kind, amount, "Accepted"))
    else:
        print("Rejected: unknown transaction type.")
        transactions.append((kind, amount, "Rejected"))

print("\nTransaction Summary")
for item in transactions:
    print(f"{item[0]} | {item[1]:.2f} | {item[2]}")
print(f"Final balance: {balance:.2f}")
print("Accepted transactions:", sum(1 for t in transactions if t[2] == "Accepted"))
print("Rejected transactions:", sum(1 for t in transactions if t[2] == "Rejected"))
