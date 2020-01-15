# 24 Game

# You have 4 cards each containing a number from 1 to 9. You need to judge whether they could operated through *, /, +, -, (, ) to get the value of 24.

# Example 1:
# Input: [4, 1, 8, 7]
# Output: True
# Explanation: (8-4) * (7-1) = 24

# Example 2:
# Input: [1, 2, 1, 2]
# Output: False

from operator import add, sub, mul, truediv
class Solution(object):
    def point24(self, numbers):
        if not numbers:
            return False
        if len(numbers) == 1:
            return abs(numbers[0] - 24) < 1e-6
        for i in range(len(numbers)):
            for j in range(len(numbers)):
                if i != j:
                    B = [numbers[k] for k in range(len(numbers)) if i != k != j]
                    for op in (truediv, mul, add, sub):
                        if op in (mul, add) and j > i:
                            continue
                        if op is not truediv or numbers[j]:
                            B.append(op(numbers[i], numbers[j]))
                            if self.point24(B):
                                return True
                            B.pop()
        return False

    def point24noparenthese(self, numbers):
        for op1 in ('+', '-', '*', '/'):
            for op2 in ('+', '-', '*', '/'):
                for op3 in ('+', '-', '*', '/'):
                    try:
                        res = eval(str(numbers[0]) + op1 + str(numbers[1]) + op2 + str(numbers[2]) + op3 + str(numbers[3]))
                    except ZeroDivisionError:
                        pass
                    else:
                        if abs(res - 24) < 1e-6:
                            return True
        return False

sol = Solution()
print(sol.point24noparenthese(numbers=[0, 6, 4, 0]))
