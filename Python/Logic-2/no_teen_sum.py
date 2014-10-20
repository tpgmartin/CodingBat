def no_teen_sum(a, b, c):
  a = a if a not in range(13,20) else fix_teen(a)
  b = b if b not in range(13,20) else fix_teen(b)
  c = c if c not in range(13,20) else fix_teen(c)

  return a + b + c

def fix_teen(n):
  return n if n == 15 or n == 16 else 0