def min_max(nums):
    return min(nums), max(nums)

low, high=min_max([1,2,3,4])

print(f"the min num is {low} and max num is {high}")