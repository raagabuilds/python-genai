def greet(name='Ram'):
    print(f"name: {name}")


greet()
greet("sam")


def power(base, exponent=2):
    return base ** exponent

print(power(5))         
print(power(5, 3))    
print(power(2, 10)) 