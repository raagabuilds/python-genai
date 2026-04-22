first_num = float(input("Enter first number: "))
second_num = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

if operation == '+':
    print(f"Result: {first_num} + {second_num} = {first_num + second_num:.2f}")
elif operation == '-':
    print(f"Result: {first_num} - {second_num} = {first_num - second_num:.2f}")
elif operation == '*':
    print(f"Result: {first_num} * {second_num} = {first_num * second_num:.2f}")
elif operation == '/':
    if second_num == 0:
        print("Cannot divide by zero")
    else:
        print(f"Result: {first_num} / {second_num} = {first_num / second_num:.2f}")
else:
    print("Invalid operation")
