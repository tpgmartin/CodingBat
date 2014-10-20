def end_other(a, b):
  lower_a = a.lower()
  lower_b = b.lower()
  return lower_a in lower_b[-len(lower_a):] or lower_b in lower_a[-len(lower_b):]
  
print end_other('Hiabc', 'abc') == True
print end_other('AbC', 'HiaBc') == True
print end_other('abc', 'abXabc') == True