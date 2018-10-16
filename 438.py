# Find All Anagrams in a String

"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""

# Hash table
# https://docs.python.org/2/library/collections.html#collections.Counter
from collections import Counter
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        lp = len(p)
        res = []
        cp = Counter(p)
        cs = Counter(s[0: lp])
        if cs == cp:
            res.append(0)
        pos = lp
        while pos < len(s):
            cs[s[pos]] += 1
            cs[s[pos - lp]] -= 1
            if cs[s[pos - lp]] == 0:
                del cs[s[pos - lp]]
            if cs == cp:
                res.append(pos - lp + 1)
            pos += 1
        return res

# Sliding Window
# http://bookshadow.com/weblog/2016/10/23/leetcode-find-all-anagrams-in-a-string/
# https://leetcode.com/problems/find-all-anagrams-in-a-string/discuss/92015/shortestconcise-java-on-sliding-window-solution
from collections import Counter
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        lp = len(p)
        cp = Counter(p)
        count = lp
        res = []
        for i in range(len(s)):
            if cp[s[i]] >= 1:
                count -= 1
            cp[s[i]] -= 1

            if i >= lp:
                if cp[s[i - lp]] >= 0:
                    count += 1
                cp[s[i - lp]] += 1

            if count == 0:
                res.append(i - lp + 1)
        return res
