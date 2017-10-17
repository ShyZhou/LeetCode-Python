# Isomorphic Strings

"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

Note:
You may assume both s and t have the same length.
"""

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict_s = {}
        dict_t = {}
        for i in range(len(s)):
            if dict_s.has_key(s[i]) and dict_s[s[i]] != t[i]:
                return False
            dict_s[s[i]] = t[i]
            if dict_t.has_key(t[i]) and dict_t[t[i]] != s[i]:
                return False
            dict_t[t[i]] = s[i]
        return True