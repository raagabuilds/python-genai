import os
def count_lines(filename):
    if not os.path.exists(filename):
        return 0
    else:
        with open(filename,"r")as f:
            count=0
            for line in f:
                line.strip()
                count+=1
        return count

print(count_lines("tasks.txt"))        
print(count_lines("exact.txt"))