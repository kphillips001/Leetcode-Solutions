# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Example:

# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Note:

# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # loop from start to end
        # if num = 0, find the next non-zero value and replace the two values
        # if non-zero value was last item => return
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                # scan forward through array until we find zero number
                j = i + 1
                while j < len(nums):
                    # keep logging until we find non zero number, break
                    if nums[j] != 0:
                        break
                    j += 1
                if j >= len(nums):
                    # The inner loop saw nothing but zeros
                    return
                # now swap values of i and j
                nums[i] = nums[j]
                nums[j] = 0
            i += 1