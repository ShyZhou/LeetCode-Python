# Add Strings

"""
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = ''
        min_len = min(len(num1), len(num2))
        add = 0
        for i in range(1, min_len+1):
            digit_sum = int(num1[-i]) + int(num2[-i]) + add
            add = 0
            if digit_sum >= 10:
                digit_sum = digit_sum - 10
                add = 1
            res = str(digit_sum) + res

        if len(num1) > min_len:
            for i in range(min_len+1, len(num1)+1):
                digit_sum = int(num1[-i]) + add
                add = 0
                if digit_sum >= 10:
                    digit_sum = digit_sum - 10
                    add = 1
                res = str(digit_sum) + res

        elif len(num2) > min_len:
            for i in range(min_len+1, len(num2)+1):
                digit_sum = int(num2[-i]) + add
                add = 0
                if digit_sum >= 10:
                    digit_sum = digit_sum - 10
                    add = 1
                res = str(digit_sum) + res

        if add == 1:
            res = '1' + res

        return res