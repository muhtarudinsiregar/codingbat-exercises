def sum2(nums):
    if len(nums) == 0:
        return 0

    return sum(nums[:2])


print(sum2([1, 2, 3]))
print(sum2([1, 1, 3]))
print(sum2([1, 1, 1, 1]))
