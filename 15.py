# 3Sum

# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
# Note:
# Elements in a triplet (a,b,c) must be in non-descending order. (ie, a <= b <= c)
# The solution set must not contain duplicate triplets.
#     For example, given array S = {-1 0 1 2 -1 -4},
#     A solution set is:
#     (-1, 0, 1)
#     (-1, -1, 2)

class Solution(object):
    def threesum(self, S, target):
        S = sorted(S)
        res = set()
        for k in range(len(S)):
            tgt = target - S[k]
            i, j = k + 1, len(S) - 1
            while i < j:
                sum_two = S[i] + S[j]
                if sum_two < tgt:
                    i += 1
                elif sum_two > tgt:
                    j -= 1
                else:
                    res.add((S[k], S[i], S[j]))
                    i += 1
                    j -= 1
        return res


sol = Solution()
print(sol.threesum(S=[-1,0,1,2,-1,-4], target=0))

# 4Sum

# Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

class Solution(object):
    def k_sum(self, nums, target, k):
        nums = sorted(nums)
        if k == 0:
            yield []
        elif k == 1:
            if target in set(nums):
                yield [target]
        elif k == 2:
            i, j = 0, len(nums) - 1
            while i < j:
                sum_two = nums[i] + nums[j]
                if sum_two < target:
                    i += 1
                elif sum_two > target:
                    j -= 1
                else:
                    yield [(nums[i], nums[j])]
                    i += 1
                    j -= 1
        else:
            for i in range(len(nums)):
                new_target = target - nums[i]
                for p in k_sum(nums=s[i + 1:], target=new_target, k=k-1):
                    yield [nums[i]] + p

# The yield statement suspends function’s execution and sends a value back to caller, but retains enough state to enable function to resume where it is left off. When resumed, the function continues execution immediately after the last yield run. This allows its code to produce a series of values over time, rather them computing them at once and sending them back like a list.
