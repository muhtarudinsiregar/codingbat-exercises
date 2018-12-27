def count_even(nums):
    count = 0

    for i in nums:
        if i % 2 == 0:
            count += 1
    return count


print(count_even([2, 1, 2, 3, 4]))
print(count_even([2, 2, 0]))
print(count_even([1, 3, 5]))
