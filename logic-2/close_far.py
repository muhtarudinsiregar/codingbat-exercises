def close_far(a, b, c):
    statement_1 = abs(a - b) <= 1 and abs(b - c) >= 2 and abs(a-c) >= 2
    statement_2 = abs(a-c) <= 1 and abs(b - c) >= 2 and abs(a-b) >= 2

    return statement_1 or statement_2


print(close_far(1, 2, 10))
print(close_far(1, 2, 3))
print(close_far(4, 1, 3))
