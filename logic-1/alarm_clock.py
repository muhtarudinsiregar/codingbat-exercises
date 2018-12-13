def alarm_clock(day, vacation):
  weekend = day == 6 or day == 0
  if vacation and weekend:
    return "off"

  if (vacation and not weekend) or (not vacation and weekend):
    return "10:00"

  return "7:00"



print(alarm_clock(1, False))
print(alarm_clock(5, False))
print(alarm_clock(0, False))
