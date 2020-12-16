# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Assume no negative numbers and no zero in array or target
# Return None if no answer

# Planning 
# Not worry about Big O for now but Brute Force
# 2 loops to generate all pairs 
# loop for each num_1 un nums:
# loop num2 in nums starting at index +1
# num_1 + num_2 -> Brute Force Approach

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                num1 = nums[i]
                num2 = nums[j]
                if num1 + num2 == target:
                    return [i, j]
        return None

# Can we come up with better solution?
# for each number, subtract the number from target. look to see if the    remainder is in the array. if not, next number ??
# Use a dictionary with key values => Ask dictionary to see if have other number. That's an O(1) operation. 
# Steps 
# Build a dictionary => loop - each num index, insert into dictionary
# Find the two numbers => For each num => is there a matching number (compliment) and where is it?

def two_sum(nums, target):
  num_dict = {}

  for i in range(len(nums)):
    num_dict[nums[i]] = i

  for i in range(len(nums)):
    current_num = nums[i]
    # check if the compliment is in dict
    compliment = target - current_num

    if compliment in num_dict and i != num_dict[compliment]:
      # compliment exists! return its index
      return [i, num_dict[compliment]]

print(two_sum(nums = [2,5,9,13], target = 7))
print(two_sum(nums = [4,3,5], target = 8))