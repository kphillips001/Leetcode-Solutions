# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# Note: For the purpose of this problem, we define empty string as valid palindrome.

# Example 1:

# Input: "A man, a plan, a canal: Panama"
# Output: true
# Example 2:

# Input: "race a car"
# Output: false
 

# Constraints:

# s consists only of printable ASCII characters.
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Palindrome - reading from the front and back are equal
        # Ignore commas, etc. Only consider alphanumeric cases, ignore strings
        l = 0
        # Reach the last value of the string
        r = len(s)-1
        # While left index is smaller than right index
        while l < r:
            #Check if not an alphanumeric character
            if not s[l].isalnum():
                # Increase left index by one
                l += 1
            # do the same in the right index
            elif not s[r].isalnum():
                #Reduce by one if not alphanumeric
                r -= 1
            # Now l and r are alpanumeric
            else:
                #Check if they are not equal
                #Ignore the cases
                if not s[l].lower() == s[r].lower():
                    return False
                else:
                    #checking index till l meets r
                    l += 1
                    r -= 1
        return True
                
        # O(n) - Time
        # O(1) - Space