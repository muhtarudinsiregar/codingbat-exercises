def make_bricks(small, big, goal):
    max_big = big * 5
    remainder = 0

    if goal <= max_big:
        remainder = goal % 5
    else:
        remainder = goal - max_big

    if remainder <= small:
        return True

    return False


print(make_bricks(3, 1, 9))

# print(make_bricks(3, 1, 8))
# print(make_bricks(3, 2, 10))
