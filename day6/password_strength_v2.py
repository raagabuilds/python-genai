import re

def get_scores(password):
    score = 0
    if len(password)>=8:
        score+=1
    if any(c.isdigit() for c in password):
        score+=1
    if any(c.isupper() for c in password):
        score+=1
    if any(c.islower() for c in password):
        score+=1
    return score


def check_password_strength(password):
    score = get_scores(password)
    if score>=4:
        return "Strong"
    elif score==3:
        return "Medium"
    elif score==2:
        return "Weak"
    else:
        return "Very Weak"
    

while True:
    x = input("Enter password (or 'quit'): ")
    if x == "quit":
        break
    print(check_password_strength(x))
    
