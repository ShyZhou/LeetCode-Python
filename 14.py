# Longest Common Prefix

# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: ["flower","flow","flight"]
# Output: "fl"

# Example 2:

# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Note:

# All given inputs are in lowercase letters a-z.

from itertools import takewhile
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        # zip(["flower","flow","flight"]) --> (('f', 'f', 'f'), ('l', 'l', 'l'), ('o', 'o', 'i'), ('w', 'w', 'g'))
        # print(tuple(zip(*strs)))
        # takewhile(lambda x: x<5, [1,4,6,4,1]) --> 1 4
        # print(list(takewhile(lambda x: len(set(x)) == 1, zip(*strs))))

        max_pre_len = len(list(takewhile(lambda x: len(set(x))==1, zip(*strs))))
        return strs[0][:max_pre_len]
