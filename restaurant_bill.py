cost=float(input("Enter meal cost: "))
weekend=input("Is it a weekend(yes/no): ").strip().lower()
card=input("Do you have loyalty card(yes/no): ").strip().lower()
tip=float(input("what is the tip percentage: "))

if weekend=="yes":
   surcharge=cost*10/100
else:
   surcharge=0

running=cost+surcharge

if card=="yes":
   loyalty=running*5/100
else:
   loyalty=0

subtotal=running-loyalty

tip_amount = subtotal*tip/100

print(f"your subtotal = ${subtotal:.2f}")
print(f"tip_amount=${tip_amount:.2f}")
print(f"final_total = ${subtotal+tip_amount:.2f}")
   
