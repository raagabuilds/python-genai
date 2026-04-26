prices = [9.99, 14.50, 22.00, 5.75, 18.30]

for price in prices:
    print(f"{price:.2f}")

total=0
for price in prices:
    total+=price
print(f"total:{total:.2f}")

print(f"Sum built-in: ${sum(prices):.2f}")
