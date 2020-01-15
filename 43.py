# Multiply Strings

# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

# Example 1:
# Input: num1 = "2", num2 = "3"
# Output: "6"

# Example 2:
# Input: num1 = "123", num2 = "456"
# Output: "56088"

# Note:
# The length of both num1 and num2 is < 110.
# Both num1 and num2 contain only digits 0-9.
# Both num1 and num2 do not contain any leading zero, except the number 0 itself.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n1, n2 = len(num1), len(num2)
        if n1 == 0 or n2 == 0:
            return ''

        num1 = num1[::-1]
        num2 = num2[::-1]

        res = [0 for _ in range(n1 + n2)]
        for j in range(n2):
            carry = 0
            d2 = int(num2[j])

            # Calculate s1 * d2
            for i in range(n1):
                d1 = int(num1[i])
                # s1[i] * s2[j] should be added into res[i+j].
                tmp = res[i + j] + d1 * d2 + carry
                carry = int(tmp / 10)
                res[i + j] = tmp - carry * 10

            # After calculation of s1*d2, we need to check if s1 * d2 has a carry at the highest position
            if carry! = 0:
                res[n1 + j] = carry

        res = ''.join(str(x) for x in res[::-1])
        i = 0
        while i < len(res) and res[i] == '0':
            i += 1
        res = res[i:]
        return '0' if len(res) == 0 else res
