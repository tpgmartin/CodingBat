def array123(nums):
  for i in range(len(nums)-2):
    if (nums[i], nums[i+1], nums[i+2]) == (1, 2, 3):
      return True
  return False

print array123([1, 1, 2, 3, 1]) == True
print array123([1, 1, 2, 4, 1]) == False
print array123([1, 1, 2, 1, 2, 3]) == True