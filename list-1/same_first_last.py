def same_first_last(nums):
    if len(nums) <= 0:
        return False

    return nums[0] == nums[- 1]

print(same_first_last([1, 2, 3]))
print(same_first_last([1, 2, 1]))
print(same_first_last([1, 2, 3, 1]))
print(same_first_last([]))
