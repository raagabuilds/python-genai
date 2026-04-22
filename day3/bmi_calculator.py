weight=float(input("Enter your weight in kg: "))
height=float(input("Enter your height in m: "))
if weight <= 0 or height <= 0:
    print("Invalid input. Weight and height must be positive.")
else:
    bmi = weight / (height * height)
    
    if bmi < 18.5:
        print(f"BMI is {bmi:.1f}. You're underweight.")
    elif bmi < 25:
        print(f"BMI is {bmi:.1f}. You're normal.")
    elif bmi < 30:
        print(f"BMI is {bmi:.1f}. You're overweight.")
    else:
        print(f"BMI is {bmi:.1f}. You're obese.")
