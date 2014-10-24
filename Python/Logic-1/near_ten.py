def near_ten(num):
  return num % 10 in [8,9,0,1,2]
  
print near_ten(12) == True
print near_ten(17) == False
print near_ten(19) == True