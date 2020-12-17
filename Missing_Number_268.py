# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #Convert the list to a set
        #Sets are used to store multiple items in a single variable. Set is one of 4 built-in data types in Python used           #to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and               #usage. A set is a collection which is both unordered and unindexed.
        num_set = set(nums)
        # original list - loop through
        for i in range(len(nums)+1):
            if i not in num_set:
                return i