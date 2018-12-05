def array123(nums):
    for i in range(len(nums)):
        if nums[i:i+3] == [1, 2, 3]:
            return True

    return False

    # or solution from codingbat
    # Note: iterate with length-2, so can use i+1 and i+2 in the loop
    #   for i in range(len(nums)-2):
    #     if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
    #       return True
    #   return False



print(array123([1, 1, 2, 3, 1]))
