age=int(input("enter your age: "))

if age<0:
    print("Invalid age")
elif age<=12:
    print("You are a Child")
elif  age<=19:
    print("You are a Teenager")
elif age<=59:
    print("You are an adult")
else:
    print("You are senior citizen")