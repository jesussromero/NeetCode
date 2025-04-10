class Solution:
    '''Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
    An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
    Ex: 
    Input: s = "racecar", t = "carrace"
    Output: true'''

    def isAnagram(self, s: str, t: str) -> bool:
        # Checking if lengths are not equal
        if len(s) != len(t):
            return False
        
        # Starting hash maps to count the characters in both strings
        # Using dictionary to count the characters in both strings
        countS, countT = {}, {}

        # Counting the characters in both strings
        # Using the get method to return 0 if the character is not found in the dictionary
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        # Return True if both dictionaries are equal, false otherwise
        return countS == countT
        