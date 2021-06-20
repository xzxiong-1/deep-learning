nums = [2, 3, 1, 0, 2, 5, 3]
lst = set(nums)
for i in range(len(nums)):
    if nums[i] not in lst:
     return nums[i]

            
            