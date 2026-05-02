def greet():
    print("Hello")

def greet_name(name):
    print(f"Hello {name}")

def add(a,b):
    return a+b

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


greet()
greet_name("ram")
print(add(5,3))
print(is_even(7))
print(is_even(4))


