# Student Attendance Record I

"""
You are given a string representing an attendance record for a student. The record only contains the following three characters:

'A' : Absent.
'L' : Late.
'P' : Present.
A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

You need to return whether the student could be rewarded according to his attendance record.

Example 1:
Input: "PPALLP"
Output: True

Example 2:
Input: "PPALLL"
Output: False
"""

class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        absent = 0
        late = 0
        for ch in s:
            if ch == 'A':
                absent = absent + 1
                if absent > 1:
                    return False
                if late > 0:
                    late = 0
            elif ch == 'L':
                late = late + 1
                if late > 2:
                    return False
            else:
                if late > 0:
                    late = 0

        return True