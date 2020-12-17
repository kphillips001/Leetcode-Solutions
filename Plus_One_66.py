# Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.

# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

# You may assume the integer does not contain any leading zero, except the number 0 itself.
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # inputs: array
        # outputs: array
        # array[-1] => last element in array = array[-1] += 1 to increment by 1
        digit_index = len(digits) - 1
        
        while digit_index >= 0:
            # add one to the current digit
            digits[digit_index] += 1
            # check if this digit overflows (to 10)
            if digits[digit_index] < 10:
                return digits 
            else:
                # this value is too large, set it to zero
                # continue the loop
                digits[digit_index] = 0
                digit_index -= 1
        # if we get here, that means
        # that we had all 9s and we still need to add 1
        return [1] + digits
        