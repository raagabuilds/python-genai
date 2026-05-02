def count_words(text):
    n=text.split(" ")
    words=len(n)
    return words

print(count_words("hello world"))               # 2
print(count_words("Python is fun and powerful"))  # 5
print(count_words(""))  