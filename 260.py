# Single Number III

"""
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

Example:
Input:  [1,2,1,3,2,5]
Output: [3,5]

Note:
The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
"""

# 假设只出现一次的两个数是 A、B，xor 一遍, 那我们最后只能得到一个值 = A xor B，但没有办法知道 A 是多少，B 是多少。
# 那得到的这个值有没有用呢？有，xor 是按位比较，相同为0，不同为1，也就是说得到的这个值里，所有的1都代表了：在这个位置上，A 和 B 是不同的，这给我们区分 A B 提供了一个方法：
#
# 我们找最右边的那个1（也就是 A和B 在这个位置上的值反正有一个是0 有一个是1，再次遍历一遍数组，按照这个位置上是0还是1分成两组，那么 A 和 B 一定会被分开。而对于其他的数字，无论他们在这个位置上是0还是1，总之他们会两两一对分到两个组中的任意一个组里去。
#
# 这就转化成了初级版本的问题了，每个组中都只有一个数出现1次，对两个组分别做一次xor，得到两个数就是 A 和 B。
import functools
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        xor = functools.reduce(lambda i, j: i ^ j, nums)
        xor &= -xor # get the last 1 of xor
        a, b = 0, 0
        for n in nums:
            if n & xor:
                a ^= n
            else:
                b ^= n
        return [a, b]
