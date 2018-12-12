def max_end3(nums):
    max = 0

    if nums[0] <= nums[len(nums) - 1]:
        max = nums[len(nums) - 1]
    else:
        max = nums[0]

    return [max] * 3

    # or
    # max_value = max(nums[0], nums[len(nums) - 1])
    # return [max_value] * 3


print(max_end3([1, 2, 3]))
print(max_end3([11, 5, 9]))
print(max_end3([2, 11, 3]))
