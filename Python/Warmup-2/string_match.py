def string_match(a, b):
  count = 0 
  for i in range(len(a)-1):
    if a[i:i+2] == b[i:i+2]:
     count += 1
  return count

print string_match('xxcaazz', 'xxbaaz') == 3
print string_match('abc', 'abc') == 2
print string_match('abc', 'axc') == 0