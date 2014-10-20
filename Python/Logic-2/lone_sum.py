def lone_sum(a, b, c):
  sum = 0
  if a != b and a != c: sum += a
  if b != a and b != c: sum += b
  if c != a and c != b: sum += c
  
  return sum

  
print lone_sum(1, 2, 3) == 6
print lone_sum(3, 2, 3) == 2
print lone_sum(3, 3, 3) == 0