fruits = ["apple", "banana", "apple", "cherry", "apple", "banana"]
target = "apple"


count=0
for f in fruits:
    if f==target:
        count+=1
print(count)

print(fruits.count(target))