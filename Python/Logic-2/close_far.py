def close_far(a, b, c):
  first = abs(a - b) <= 1 and abs(a - c) > 1 and abs(b - c) > 1 
  second = abs(a - c) <= 1 and abs(a - b) > 1 and abs(b - c) > 1 
  return first or second

print close_far(1, 2, 10) == True
print close_far(1, 2, 3) == False
print close_far(4, 1, 3) == True