def xyz_there(str):
  for i in range(len(str)):
    if str[i] != '.' and str[i+1:i+4] == 'xyz':
      return True
  if str[0:3] == 'xyz':
      return True
  return False
  
print xyz_there('abcxyz') == True
print xyz_there('abc.xyz') == False
print xyz_there('xyz.abc') == True