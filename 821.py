# Shortest Distance to a Character

"""
Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

Example 1:
Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]

Note:
S string length is in [1, 10000].
C is a single character, and guaranteed to be in string S.
All letters in S and C are lowercase.
"""

class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        res = [0] * len(S)
        pre = -len(S)
        next_pos = S.find(C)
        for i in range(len(S)):
            if S[i] == C:
                pre = i
                next_pos = S.find(C, i+1)
                if next_pos < 0:
                    next_pos = -len(S)
            res[i] = min(i - pre, abs(i - next_pos))
        return res
