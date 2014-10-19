def max_end3(nums):
    return [ max(nums[0], nums[-1]) for num in nums ]

print max_end3([5,2,3])