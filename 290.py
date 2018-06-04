# Word Pattern

"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.
"""

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        pattern_to_str = {}
        str_to_pattern = {}
        words = str.split(' ')
        if len(pattern) != len(words):
            return False

        for i in range(0, len(pattern)):
            if pattern[i] in pattern_to_str:
                if pattern_to_str[pattern[i]] != words[i]:
                    return False
            else:
                pattern_to_str[pattern[i]] = words[i]

            if words[i] in str_to_pattern:
                if str_to_pattern[words[i]] != pattern[i]:
                    return False
            else:
                str_to_pattern[words[i]] = pattern[i]

        return True