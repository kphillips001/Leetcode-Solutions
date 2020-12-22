# Given a string s consists of some words separated by spaces, return the length of the last word in the string. If the last word does not exist, return 0.

# A word is a maximal substring consisting of non-space characters only.
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if s == '':
            return 0
        s = s.split()
        if not s:
            return 0
        return len(s[-1])``