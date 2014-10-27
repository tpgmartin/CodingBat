def sum13(nums): 
  for i in range(len(nums)):
    if nums[i] == 13:
      nums[i] = 0
      if i+1 < len(nums): 
        nums[i+1] = 0
        
  return sum(nums)
  
print sum13([1, 2, 2, 1]) == 6
print sum13([1, 1]) == 2
print sum13([1, 2, 2, 1, 13]) == 6
