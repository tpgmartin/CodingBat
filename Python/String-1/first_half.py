def first_half(str):
  if (len(str) % 2 == 0):
    return str[:len(str)/2]
  else:
    return str[:(len(str)+1)/2]

print first_half('WooHoo')
print first_half('HelloThere')
print first_half('abcdef')