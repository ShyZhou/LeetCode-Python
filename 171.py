# Excel Sheet Column Number

"""
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
"""

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for i in range (0, len(s)):
            res += (ord(s[i]) - ord('A') + 1) * 26 ** (len(s) - 1 - i)
        return res