# Maximum Product Subarray

"""
Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
"""

# Space limit exceeds, O(n*n) space, O(n*n) time
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        product = [[None] * len(nums) for i in range(len(nums))]

        for i in range(len(nums)):
            product[i][i] = nums[i]
            if i > 0:
                for r in range(i):
                    product[r][i] = product[r][i-1] * nums[i]

        max = None
        max_b = 0
        max_e = 0
        for r in range(len(nums)):
            for c in range(r, len(nums)):
                if product[r][c] >= max:
                    max, max_b, max_e = product[r][c], r, c

        return max

# Time limit exceeds, O(n*n) time
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > max:
                max = nums[i]
            if nums[i] != 1:
                for r in range(i):
                    nums[r] = nums[r] * nums[i]
                    if nums[r] > max:
                        max = nums[r]

        return max

# DP, O(n) time, O(n) space
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_product = [None] * len(nums)
        min_product = [None] * len(nums)
        max_product[0] = nums[0]
        min_product[0] = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > 0:
                max_product[i] = max(max_product[i-1] * nums[i], nums[i])
                min_product[i] = min(min_product[i-1] * nums[i], nums[i])
            elif nums[i] < 0:
                max_product[i] = max(min_product[i-1] * nums[i], nums[i])
                min_product[i] = min(max_product[i-1] * nums[i], nums[i])
            else:
                max_product[i] = 0
                min_product[i] = 0

            res = max(res, max_product[i])

        return res

# DP, O(n) time, O(1) space
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_product= nums[0]
        min_product = nums[0]
        res = nums[0]

        for n in nums[1:]:
            max_tmp = max_product
            min_tmp = min_product
            max_product = max(max_tmp * n, min_tmp * n, n)
            min_product = min(max_tmp * n, min_tmp * n, n)
            res = max(res, max_product)

        return res