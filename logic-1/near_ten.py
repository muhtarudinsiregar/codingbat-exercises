def near_ten(num):
  return num % 10 in [0,1,2,8,9,10]

print(near_ten(19))
print(near_ten(12))
