# Integer Break

"""
Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

Example 1:

Input: 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.

Example 2:
Input: 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.

Note: You may assume that n is not less than 2 and not larger than 58.
"""

# DP, O(n^2)
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        max_prod = [0] * (n + 1)
        for num in range(2, n + 1):
            max_prod[num - 1] = max(max_prod[num - 1], num - 1)
            for i in range(1, int(num / 2) + 1):
                max_prod[num] = max(max_prod[i] * max_prod[num - i], max_prod[num])
        return max_prod[n]

# O(n)
# 正整数从1开始，但是1不能拆分成两个正整数之和，所以不能当输入。

# 那么2只能拆成 1+1，所以乘积也为1。

# 数字3可以拆分成 2+1 或 1+1+1，显然第一种拆分方法乘积大为2。

# 数字4拆成 2+2，乘积最大，为4。

# 数字5拆成 3+2，乘积最大，为6。

# 数字6拆成 3+3，乘积最大，为9。

# 数字7拆为 3+4，乘积最大，为 12。

# 数字8拆为 3+3+2，乘积最大，为 18。

# 数字9拆为 3+3+3，乘积最大，为 27。

# 数字10拆为 3+3+4，乘积最大，为 36。

# ....

# 那么通过观察上面的规律，我们可以看出从5开始，数字都需要先拆出所有的3，一直拆到剩下一个数为2或者4，因为剩4就不用再拆了，拆成两个2和不拆没有意义，而且4不能拆出一个3剩一个1，这样会比拆成 2+2 的乘积小。这样我们就可以写代码了，先预处理n为2和3的情况，然后先将结果 res 初始化为1，然后当n大于4开始循环，结果 res 自乘3，n自减3，根据之前的分析，当跳出循环时，n只能是2或者4，再乘以 res 返回即可
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 3:
            return n - 1
        res = 1
        while n > 4:
            res *= 3
            n -= 3
        return res * n
