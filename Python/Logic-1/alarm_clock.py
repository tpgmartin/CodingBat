def alarm_clock(day, vacation):
  if day in range(1,6):
    return '10:00' if vacation else '7:00'
  else:
    return 'off' if vacation else '10:00'
  
print alarm_clock(1, False) == '7:00'
print alarm_clock(5, False) == '7:00'
print alarm_clock(0, False) == '10:00'