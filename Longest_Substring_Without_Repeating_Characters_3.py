# Given a string s, find the length of the longest substring without repeating characters.

# Constraints:

#     0 <= s.length <= 5 * 104
#     s consists of English letters, digits, symbols and spaces.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # use dictionary and check to see if letter is already in dict. 
        # Make empty dictionary
        sub = {}
        # Keep track of index where current substring is starting from => start it at zero  
        curr_sub_start = 0
        # Keep track of current length of substring and the longest we've seen thus far
        curr_len = 0
        longest = 0
        # Create loop - takes index and letter for each letter in string
        for i, letter in enumerate(s):
            # Is letter already in dictionary and index postion - stored at sub[letter] 
            # Looking up where index of letter is. Is index >= our current sub string index. If so, we have a duplicate
            if letter in sub and sub[letter] >= curr_sub_start:
                # Set start of new substring 1 after the letter that was the duplicate
                curr_sub_start = sub[letter] + 1
                # Update current length of substring, since we ran into a duplicate 
                # Update current length to current index positon we're at minus the index position of the duplicate we saw
                curr_len = i - sub[letter]
                # Update index of letter we're looking at
                sub[letter] = i
            # if we haven't seen the letter at all, will add letter to index 
            else:
                sub[letter] = i
            # iterate the current length
                curr_len += 1
            # check to see if current substring we're looking at when we just added new letter is longer than the longest 
            # we've seen thus far
                if curr_len > longest:
                # Update the longest to equal our substring length
                    longest = curr_len
        return(longest)




# https://www.youtube.com/watch?v=sUicrnHwA0s
