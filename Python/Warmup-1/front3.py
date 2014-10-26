def front3(str):
  return 3 * str[:3]

print front3('Java') == 'JavJavJav'
print front3('Chocolate') == 'ChoChoCho'
print front3('abc') == 'abcabcabc'