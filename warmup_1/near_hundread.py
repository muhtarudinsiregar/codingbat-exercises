def near_hundread(n):
    return (abs(100 - n) <= 10) or (abs(200 - n) <= 10)

print(near_hundread(89))
print(near_hundread(90))
print(near_hundread(190))
print(near_hundread(189))
