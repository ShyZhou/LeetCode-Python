# Maximum Product of Word Lengths

"""
Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.

Example 1:
Input: ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16
Explanation: The two words can be "abcw", "xtfn".

Example 2:
Input: ["a","ab","abc","d","cd","bcd","abcd"]
Output: 4
Explanation: The two words can be "ab", "cd".

Example 3:
Input: ["a","aa","aaa","aaaa"]
Output: 0
Explanation: No such pair of words.
"""

class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
       	words_set = [set(w) for w in words]
        l = len(words)
        res = 0
        for i in range(l):
            li = len(words[i])
            for j in range(i+1, l):
                if words_set[j].isdisjoint(words_set[i]):
                    res = max(len(words[j]) * li, res)
        return res
