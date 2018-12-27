def centered_average(nums):

    sum = 0
    for element in nums:
        sum += element
    return (sum - min(nums) - max(nums)) / (len(nums)-2)


print(centered_average([1, 2, 3, 4, 100]))
print(centered_average([1, 1, 5, 5, 10, 8, 7]))
print(centered_average([-10, -4, -2, -4, -2, 0]))
