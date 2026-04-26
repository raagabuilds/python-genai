nums = [12, 45, 7, 23, 89, 34, 56, 78]

largest=nums[0]

for n in nums:
    if largest<n:
        largest=n
print(largest)   
print(max(nums))     
        

