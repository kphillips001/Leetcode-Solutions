# Given an array of integers, find if the array contains any duplicates.

# Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Brute Force - Two Loops
        for i in range (len(nums)):
            for j in range (i + 1, len(nums)):
                # Compare if current i value is equal to j value
                if nums[i] == nums[j]:
                    return True
            return False

# Second solution - use dictionary
# Get rid of second loop
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for i in range (len(nums)):
          if dict.get(nums[i]) is not None:
            return True
          else:
            dict[nums[i]] = 2
        return False
                
# Third solution - Used sorted method
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        for i in range(1, len(nums)):
          if nums[i] == nums[i-1]:
            return True
        return False
                