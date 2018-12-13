def sorta_sum(a, b):
    sum = sum(a, b)
    if 10 <= sum <= 20:
        return 20

    return sum


print(sorta_sum(3, 4))
print(sorta_sum(9, 4))
print(sorta_sum(10, 11))
