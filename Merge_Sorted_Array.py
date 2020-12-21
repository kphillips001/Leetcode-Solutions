# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

# Note:

# The number of elements initialized in nums1 and nums2 are m and n respectively.
# You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.
# Example:

# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3

# Output: [1,2,2,3,5,6]
 

# Constraints:

# -10^9 <= nums1[i], nums2[i] <= 10^9
# nums1.length == m +

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Merge nums2 into nums1 as sorted array
        # There's enough space in nums1 to hold all elments in nums2. Empty space is at the end of Nums1
        # So, merge from the rear first where the empty spaces reside
        # Put the largest value at the very end of nums1 => start at last real value in nums1 and last num in nums2
        # Compare the two values, then do the same with second to last number
        # M & N are the index of the last value(nums1, nums2)
        
        # Get last index of nums1 (this is the length) 
        last = m + n - 1
        
        # merge in reverse order
        # loop while elements left in both arrays
        while m > 0 and n > 0:
            # find the largest value (Index start as zero)
            if nums1[m - 1] > nums2[n - 1]:
                # Go to last position and replace
                nums1[last] = nums1[m - 1]
                # Update the pointer
                m -= 1
                # Else if are equal or if nums2 is greater => do the oppososite
            else:
                nums1[last] = nums2[n - 1]
                # Update the pointer
                n -= 1
                # Also need to decrement last 
            last -= 1
        # fill nums1 with leftover element in nums2 if there are leftover elements
        while n > 0:
            nums1[last] = nums2[n - 1]
            # update pointers
            n, last = n - 1, last - 1