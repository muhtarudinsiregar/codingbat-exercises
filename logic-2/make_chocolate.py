def make_chocolate(small, big, goal):
    max_bars = big * 5
    remainder = 0

    if max_bars <= goal:
        remainder = goal - max_bars
    else:
        remainder = goal % 5

    if remainder <= small:
        return remainder

    return -1


# print(make_chocolate(4, 1, 9))
# print(make_chocolate(4, 1, 10))
# print(make_chocolate(4, 1, 7))
# print(make_chocolate(6, 1, 10))
print(make_chocolate(1, 2, 7))
