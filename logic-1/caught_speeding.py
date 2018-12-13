def caught_speeding(speed, is_birthday):
  if is_birthday:
    speed -= 5 #daripada menaikkan batas kecepatan, lebih baik speed yg dikurangi dengan 5

  if speed >= 81:
    return 2

  if speed <= 60:
    return 0
  return 1

print(caught_speeding(60, False))
print(caught_speeding(65, False))
print(caught_speeding(65, True))
