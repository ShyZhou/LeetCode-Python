# Shuffle an Array

"""
Shuffle a set of numbers without duplicates.

Example:

// Init an array with set 1, 2, and 3.
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
solution.shuffle();

// Resets the array back to its original configuration [1,2,3].
solution.reset();

// Returns the random shuffling of array [1,2,3].
solution.shuffle();
"""

import random
class Solution(object):
    original_nums = None
    # permutation_num = 0

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.original_nums = nums
        # self.permutation_num = math.factorial(len(nums))


    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.original_nums


    # Use existing module
    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        res = self.original_nums[:]
        random.shuffle(res)
        return res


    # Fisher–Yates shuffle algorithm
    # To shuffle an array a of n elements (indices 0..n-1):
    # for i from n−1 downto 1 do
    #     j ← random integer such that 0 ≤ j ≤ i
    #     exchange a[j] and a[i]
    def shuffle(self):
        res = self.original_nums[:]
        for i in reversed(range(1, len(res))):
            j = random.randrange(i+1)
            res[i], res[j] = res[j], res[i]
        return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()