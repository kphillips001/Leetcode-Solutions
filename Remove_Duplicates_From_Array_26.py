# Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.

# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

# Clarification:

# Confused why the returned value is an integer but your answer is an array?

# Note that the input array is passed in by reference, which means a modification to the input array will be known to the caller as well.

# Internally you can think of this:

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Cannot use this solution below. Must modify the input array in-place
        # nums = set(nums)
        i = 0
        # use while loop
        while i < len(nums):
            # i to the very end
            if nums[i] in nums[i+1:]:
                # if in that range, then remove
                nums.remove(nums[i])
            else:
                # if not, increment to get to next index
                i += 1
                # Don't return anything as pass by reference 
         
 