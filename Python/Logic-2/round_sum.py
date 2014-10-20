def round_sum(a, b, c):
  a = round10(a)
  b = round10(b)
  c = round10(c)
  return a + b + c

def round10(num):
  tens = num - num % 10
  return tens if num % 10 < 5 else tens + 10