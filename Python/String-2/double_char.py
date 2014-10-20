def double_char(str):
  output = ''
  for char in str:
      output += char * 2
  return output
  
print double_char('The') == 'TThhee'
print double_char('AAbb') == 'AAAAbbbb'
print double_char('Hi-There') == 'HHii--TThheerree'