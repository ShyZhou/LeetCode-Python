# Basic Calculator

# I

# Implement a basic calculator to evaluate a simple expression string.

# The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negativeintegers and empty spaces .

# Example 1:
# Input: "1 + 1"
# Output: 2

# Example 2:
# Input: " 2-1 + 2 "
# Output: 3

# Example 3:
# Input: "(1+(4+5+2)-3)+(6+8)"
# Output: 23

# II

# The expression string contains only non-negativeintegers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

# Example 1:
# Input: "3+2*2"
# Output: 7

# Example 2:
# Input: " 3/2 "
# Output: 1

# Example 3:
# Input: " 3+5 / 2 "
# Output: 5

# III

# The expression string contains only non-negative integers, +, -, *, / operators , open ( and closing parentheses ) and empty spaces .
# The integer division should truncate toward zero.

# "1 + 1" = 2
# " 6-4 / 2 " = 4
# "2*(5+5*2)/3+(6/2+8)" = 21
# "(2+6* 3+5- (3*14/7+2)*5)+3"=-12

class Solution(object):
    def calculator1(self, input):
        input= ''.join(c for c in input if c not in '() ')
        inputs = input.split('+')
        res = 0
        for e in inputs:
            if '-' in e:
                a, b = e.split('-')
                res += int(a)
                res -= int(b)
            else:
                res += int(e)
        return res

    def calculator2(self, input):
        stack = []
        sign = '+'
        num = 0
        for i in range(len(input)):
            c = input[i]
            if c.isdigit():
                num = 10 * num + int(c)
            if c in ('+', '-', '*', '/') or i == len(input) - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack[-1] = stack[-1] * num
                elif sign == '/':
                    stack[-1] = int(stack[-1] / num)
                sign = c
                num = 0
        return sum(stack)

    def calculator3(self, input):
        n = len(input)
        num = 0
        cur_res, res = 0, 0
        op = '+'

        i = 0
        while i < n:
            c = input[i]
            if c.isdigit():
                num = 10 * num + int(c)
            elif c == '(':
                j = i
                cnt = 0
                while i < n:
                    if input[i] == '(':
                        cnt += 1
                    if input[i] == ')':
                        cnt -= 1
                    if cnt == 0:
                        break
                    i += 1
                num = self.calculator3(input=input[j + 1: i])

            if c in ('+', '-', '*', '/') or i == n - 1:
                if op == '+':
                    cur_res += num
                elif op == '-':
                    cur_res -= num
                elif op == '*':
                    cur_res *= num
                elif op == '/':
                    cur_res = int(cur_res / num)

                if c == '+' or c == '-' or i == n - 1:
                    res += cur_res
                    cur_res = 0

                op = c
                num = 0

            i += 1
        return res




sol = Solution()
print(sol.calculator1(input='(1+(4+5+2)-3)+(6+8)'))
print(sol.calculator2(input=' 3+5 / 2 '))
print(sol.calculator3(input='(2+6* 3+5- (3*14/7+2)*5)+3'))
