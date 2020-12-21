# Given an array of positive integers arr, calculate the sum of all possible odd-length subarrays.

# A subarray is a contiguous subsequence of the array.

# Return the sum of all odd-length subarrays of arr.

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        # Store the sum
        sum = 0
        # Size of the array
        l = len(arr)
        # Traverse the array
        for i in range(l):
            # Generate all subarray of odd length
            for j in range(i, l, 2):
                for k in range(i, j+1, 1):
                    #Add the element to sum
                    sum += arr[k]
        return sum