# Number of Segments in a String

"""
Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.

Please note that the string does not contain any non-printable characters.

Example:

Input: "Hello, my name is John"
Output: 5
"""

class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = 0
        pre = ''
        for c in s:
            if c == ' ' and pre != '' and pre != ' ':
                cnt += 1
            pre = c

        if pre == '':
            return 0
        else:
            return cnt if pre == ' ' else cnt + 1
