bill=float(input("Enter your bill:" ))
percentage=int(input("enter the percentage of tip: "))

tip=(bill*percentage)/100
print(f"The total bill is {bill+tip:.2f}")