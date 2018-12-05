# Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.

def array_front9(nums):
    lists = nums[0:4]
    return 9 in lists

    # or alternative answer
    # end = len(nums)
    # if len > 4:
    #     end = 4

    # for i in range(end):
    #     if i == 9:
    #         return True
    #     return False



print(array_front9([1, 2, 3, 5, 9]))
