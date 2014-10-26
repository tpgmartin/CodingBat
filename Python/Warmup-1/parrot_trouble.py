def parrot_trouble(talking, hour):
  return talking and hour not in range(7,21)

print parrot_trouble(True, 6) == True
print parrot_trouble(True, 7) == False
print parrot_trouble(False, 6) == False