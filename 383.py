# Ransom Note

"""
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
"""

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dictionary = {}
        for i in range(0, len(magazine)):
            dictionary[magazine[i]] = 1 if magazine[i] not in dictionary else dictionary[magazine[i]] + 1
        for i in range(0, len(ransomNote)):
            if ransomNote[i] not in dictionary:
                return False
            dictionary[ransomNote[i]] -= 1
            if dictionary[ransomNote[i]] == -1:
                return False
        return True
