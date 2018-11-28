def diff21(n):
    diff = 21 - n

    if n > 21:
        diff = diff * 2
    return abs(diff)

print(diff21(10))
