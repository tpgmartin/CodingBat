def front_times(str, n):
  return n * str[:3]

print front_times('Chocolate', 2) == 'ChoCho'
print front_times('Chocolate', 3) == 'ChoChoCho'
print front_times('Abc', 3) == 'AbcAbcAbc'