# Given two strings s and t , write a function to determine if t is an anagram of s.
# Using a hash map
# Hash table is a data structure that implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index, also called a hash code, into an array of buckets or slots, from which the desired value can be found. 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Create an empty hash map
        h = {}
        # Iterating through first string, count number of times each character appears in that string
        for ch in s:
            if ch not in h:
                h[ch] = 0
            h[ch] += 1
        # Iterating through second string, decrement number of times each character appears in that string
        for ch in t:
            if ch not in h:
                h[ch] = 0
            h[ch] -= 1
        # Iterate through all the keys in hash map. If any contain key not equal to zero, return false
        for key in h.keys():
            if h[key] != 0:
                return False
        
        return True

# https://www.youtube.com/watch?v=1ns7UFp1o54