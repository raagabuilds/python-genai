fruits=["apple", "banana", "cherry","date"]
print(fruits[0])
print(len(fruits))
print(fruits[-1])

fruits.append("elderberry")
fruits.insert(0,"honey")
print(fruits)

fruits.remove("banana")
last=fruits.pop()
print(fruits)
print(f"popped:{last}")
