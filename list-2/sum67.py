def sum67(nums):
    status = False
    if len(nums) == 0:
        return 0

    for i in range(len(nums)):
        if nums[i] == 6:
            status = True
        if status and nums[i] == 7:
            nums[i] = 0
            status = False
        if status:
            nums[i] = 0
    return sum(nums)


print(sum67([1, 2, 2]))
print(sum67([1, 2, 2, 6, 99, 99, 7]))
print(sum67([1, 1, 6, 7, 2]))
print(sum67([11, 6, 7, 11]))
print(sum67([1, 6, 7, 7]))
