# Given a non-negative integer num, return the number of steps to reduce it to zero. If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.
class Solution:
    def numberOfSteps (self, num: int) -> int:
        # initialize count to zero
        count = 0
        # while loop 
        while num != 0:
            # if even
            if num % 2 == 0:
                # divide by 2
                num = num // 2
            # if odd
            else:
                #num equal to itself minus one
                num -= 1
            #increment count by one
            count += 1
        return count