class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # create dictionary to store number as the key and the count as the value
        dic = {}
        # populate dictionary with loop
        for num in nums:
            #if number not already in dictionary
            if num not in dic:
                #Assign new key of that number and count of one
                dic[num] = 1
                #Otherwise, we've already seen this number (number that appears twice) => increment value by one
            else:
                dic[num] += 1
        
        # Once dictionary is created like above, all we have to do is iterate through our dictionary and see where the              #value is one and return that key
        for key, val in dic.items():
            # When value = 1 => return that key
            if val == 1:
                return key
    # O(n) - time and space complexity