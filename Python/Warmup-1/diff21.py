def diff21(n):
  return 2 * (n-21) if n > 21 else 21 - n

print diff21(19) == 2
print diff21(10) == 11
print diff21(21) == 0