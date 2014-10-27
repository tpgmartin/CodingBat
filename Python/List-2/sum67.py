def sum67(nums):
  if (6 in nums):
    index_6 = nums.index(6)
    index_7 = nums[index_6:].index(7) + index_6 
    del nums[index_6:index_7+1]
    sum67(nums)
  return sum(nums)
  
print sum67([1, 2, 2]) == 5
print sum67([1, 2, 2, 6, 99, 99, 7]) == 5
print sum67([1, 1, 6, 7, 2]) == 4
print sum67([1, 6, 2, 6, 2, 7, 1, 6, 99, 99, 7]) == 2
print sum67([1, 6, 2, 2, 7, 1, 6, 99, 99, 7]) == 2
print sum67([6, 7, 1, 6, 7, 7]) == 8
print sum67([2, 7, 6, 2, 6, 2, 7]) == 9