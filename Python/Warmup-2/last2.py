def last2(str):
  count = 0
  for num in range(len(str)-2):
    if str[num:num+2] == str[-2:]:
      count += 1  
  return count


print last2('hixxhi') == 1
print last2('xaxxaxaxx') == 1
print last2('axxxaaxx') == 2