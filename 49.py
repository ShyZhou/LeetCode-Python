# Group Anagrams

# Given an array of strings, group anagrams together.

# Example:

# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]

import collections
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = collections.defaultdict(list)
        for s in strs:
            ss = ''.join(sorted(s))
            groups[ss].append(s)
        return groups.values()

sol = Solution()
print(sol.groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
