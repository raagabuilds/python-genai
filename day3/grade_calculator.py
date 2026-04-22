score=int(input("Enter your score: "))

if score>=0 and score<=39:
  print(f"{score} - Fail, Please try again")
elif score>=90:
  print(f"{score} - Grade A, Great Job!")
elif score>=75 :
  print(f"{score} -  Grade B, You passed")
elif score>=60 :
  print(f"{score} - Grade C, You passed")
elif score>= 40 :
  print(f"{score} - Grade D, You need to improve")
else:
  print("Invalid score")

