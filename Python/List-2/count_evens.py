def count_evens(nums):
  return len([num for num in nums if not num % 2])
  
print count_evens([2, 1, 2, 3, 4]) == 3
print count_evens([2, 2, 0]) == 3
print count_evens([1, 3, 5]) == 0