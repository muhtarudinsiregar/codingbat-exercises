def sum13(nums):
    if len(nums) == 0:
        return 0

    for i in range(0, len(nums)):
        print(nums[i] == 13, i+1 < len(nums))
        if nums[i] == 13 and i+1 < len(nums):
            nums[i] = 0
            nums[i+1] = 0
            # if:
    return sum(nums)


print(sum13([1, 2, 2, 1, 13]))
# print(sum13([13, 1, 2, 13, 2, 1, 13]))
# print(sum13([1, 2, 2, 1]))
# print(sum13([1, 1]))
# print(sum13([1, 2, 2, 1, 13]))
