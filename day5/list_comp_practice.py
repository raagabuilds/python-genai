cubes = [n*n*n for n in range(1,11)]
print(cubes)

words = ["hello", "world", "python"]
upper = [word.upper() for word in words]
print(upper)

words = ["data", "engineering", "is", "fun"]
lengths = [len(word) for word in words]
print(lengths)

divs = [n for n in range(1,31) if n%3==0]
print(divs)

sq_evens = [n*n for n in range(1,21) if n%2==0]
print(sq_evens)