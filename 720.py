# Longest Word in Dictionary

"""
Given a list of strings words representing an English Dictionary, find the longest word in words that can be built one character at a time by other words in words. If there is more than one possible answer, return the longest word with the smallest lexicographical order.

If there is no answer, return the empty string.

Example 1:
Input:
words = ["w","wo","wor","worl", "world"]
Output: "world"
Explanation:
The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".

Example 2:
Input:
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
Output: "apple"
Explanation:
Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".

Note:
All the strings in the input will only contain lowercase letters.
The length of words will be in the range [1, 1000].
The length of words[i] will be in the range [1, 30].
"""

class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        res = []
        res_len = 0
        words = set(words)
        for w in words:
            l = len(w)
            if l < res_len:
                continue
            for i in range(1, l + 1):
                if w[:i] not in words:
                    break
            else:
                if l > res_len:
                    res_len = l
                    res = [w]
                elif l == res_len:
                    res.append(w)
        return '' if not res else sorted(res)[0]
