# Minimum Moves to Equal Array Elements

"""
Given a non-empty integer array of size n, find the minimum number of moves required to make all array elements equal, where a move is incrementing n - 1 elements by 1.

Example:

Input:
[1,2,3]

Output:
3

Explanation:
Only three moves are needed (remember each move increments two elements):

[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
"""

# Naive solution, Time Limit Exceeded
class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        moves = 0
        while 1:
            if len(set(nums)) == 1:
                return moves
            nums.sort()
            for i in range(n - 1):
                nums[i] = nums[i] + 1
            moves += 1

# 1. 已知：数列nums，初始和s0，长度n，最小的数为m
# 2. 假设移动k步
# 3. 每移动一步，n-1个数会被＋1，则最终和s = s0 +(n-1) x k
#     平均数为 s/n
#     最小数每次移动都被+1，因此有：k =s/n -m
#     即：（s0 +(n-1) x k）/n -m =k
# 4. 求得： k = s0 - m x n
class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums) - len(nums) * min(nums)