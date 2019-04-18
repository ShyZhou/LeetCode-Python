# To Lower Case

"""
Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

Example 1:
Input: "Hello"
Output: "hello"

Example 2:
Input: "here"
Output: "here"

Example 3:
Input: "LOVELY"
Output: "lovely"
"""

class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        res = ''
        for c in str:
            ascii = ord(c)
            if 65 <= ascii <= 90:
                c = chr(ascii + 32)
            res += c
        return res
