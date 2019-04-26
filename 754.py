# Reach a Number

"""
You are standing at position 0 on an infinite number line. There is a goal at position target.

On each move, you can either go left or right. During the n-th move (starting from 1), you take n steps.

Return the minimum number of steps required to reach the destination.

Example 1:
Input: target = 3
Output: 2
Explanation:
On the first move we step from 0 to 1.
On the second step we step from 1 to 3.

Example 2:
Input: target = 2
Output: 3
Explanation:
On the first move we step from 0 to 1.
On the second move we step  from 1 to -1.
On the third move we step from -1 to 2.

Note:
target will be a non-zero integer in the range [-10^9, 10^9].
"""

# Math
# Observation:
# 1. Steps(n) = Steps(-n)
# 2. +/- 1 +/- 2 +/- 3 +/- ... +/- k = target
#
# To find smallest k, use + only
# 1 + 2 + 3 + ... + k = target + d, (0 <= d < k)
#
# 1. if d == 0: k is the answer
# 2. if d % 2 == 0: 1 + 2 + 3 + ... - i + ... + k = target, i = d/2
# 3. if d % 2 == 1:
#     a. k % 2 == 0, 1 + 2 + 3 + ... - i + ... + k + (k + 1) = target, i = ((k+1)+d)/2 <= k
#     b. k % 2 == 1, 1 + 2 + 3 + ... - i + ... + k - (k + 1) + (k + 2) = target, i = ((k+2)-(k+1)+d)/2 = (d+1)/2 <= k

class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        target = abs(target)
        k = 0
        while target > 0:
            k += 1
            target -= k
        return k if target % 2 == 0 else k + 1 + k % 2
