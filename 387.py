# First Unique Character in a String

"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.

Note: You may assume the string contain only lowercase letters.
"""

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        indexes = {}
        for i in range(0, len(s)):
            if s[i] in indexes:
                indexes.update({s[i]: len(s)})
            else:
                indexes.update({s[i]: i})
        v = indexes.values()
        v.sort()
        return -1 if len(v) == 0 or v[0] == len(s) else v[0]