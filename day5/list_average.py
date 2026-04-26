scores = [78, 92, 65, 88, 91, 73, 84]
if len(scores) == 0:
    print("No scores to average.")
else:
    average = sum(scores) / len(scores)
    print(f"Average: {average:.2f}")