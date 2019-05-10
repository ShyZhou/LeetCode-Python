# Basic Calculator II

"""
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Example 1:
Input: "3+2*2"
Output: 7

Example 2:
Input: " 3/2 "
Output: 1

Example 3:
Input: " 3+5 / 2 "
Output: 5

Note:
You may assume that the given expression is always valid.
Do not use the eval built-in library function.
"""

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.replace(' ', '')
        i, j = 0, 0
        nums = []
        op = '+'
        while j < len(s):
            if s[j] in ['+', '-', '*', '/'] or j == len(s) - 1:
                new_num = int(s[i: j]) if j < len(s) - 1 else int(s[i:])
                if op == '+':
                    nums.append(new_num)
                elif op == '-':
                    nums.append(-new_num)
                else:
                    nums.append(nums.pop() * new_num if op == '*' else int(float(nums.pop()) / new_num))
                op = s[j]
                i = j + 1
            j += 1
        return sum(nums)
