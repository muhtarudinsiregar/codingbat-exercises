import math


def round_sum(a, b, c):
    a_round = round10(a)
    b_round = round10(b)
    c_round = round10(c)

    print(a_round + b_round + c_round)


def round10(num):
    mod10 = num % 10
    if mod10 >= 5:
        return num - mod10 + 10
    return num - mod10


round_sum(16, 17, 18)
round_sum(12, 13, 14)
round_sum(6, 4, 4)
