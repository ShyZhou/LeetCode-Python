# Fraction to Recurring Decimal

"""
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

Example 1:
Input: numerator = 1, denominator = 2
Output: "0.5"

Example 2:
Input: numerator = 2, denominator = 1
Output: "2"

Example 3:
Input: numerator = 2, denominator = 3
Output: "0.(6)"
"""

class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        negative_res = True if (numerator > 0 and denominator < 0) or (numerator < 0 and denominator > 0) else False
        numerator = abs(numerator)
        denominator = abs(denominator)
        res = ''
        is_fraction = False
        numerator_list = []
        while numerator:
            quotient = numerator / denominator
            remainder = numerator % denominator
            new_numerator = remainder * 10
            if not is_fraction:
                res += str(quotient) + '.'
                is_fraction = True
            else:
                if new_numerator in numerator_list:
                    pos = len(numerator_list) - numerator_list.index(new_numerator)
                    res = res[:-pos] + '(' + res[-pos:]
                    res += ')' if str(quotient) == res[-1] else str(quotient) + ')'
                    break
                else:
                    numerator_list.append(numerator)
                    res += str(quotient)
            numerator = new_numerator
        if res == '':
            res = '0'
        res = res[:-1] if res[-1] == '.' else res
        return '-' + res if negative_res else res
