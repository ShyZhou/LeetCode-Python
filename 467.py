# Unique Substrings in Wraparound String

"""
Consider the string s to be the infinite wraparound string of "abcdefghijklmnopqrstuvwxyz", so s will look like this: "...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".

Now we have another string p. Your job is to find out how many unique non-empty substrings of p are present in s. In particular, your input is the string p and you need to output the number of different non-empty substrings of p in the string s.

Note: p consists of only lowercase English letters and the size of p might be over 10000.

Example 1:
Input: "a"
Output: 1
Explanation: Only the substring "a" of string "a" is in the string s.

Example 2:
Input: "cac"
Output: 2
Explanation: There are two substrings "a", "c" of string "cac" in the string s.

Example 3:
Input: "zab"
Output: 6
Explanation: There are six substrings "z", "a", "b", "za", "ab", "zab" of string "zab" in the string s.
"""

# Remember all legit substrings, Memory Limit Exceeded
import itertools
class Solution(object):
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        i, s = 0, 0
        res = set()
        while i < len(p):
            if i+1 < len(p) and ord(p[i + 1]) - 97 == (ord(p[i]) + 1 - 97) % 26:
                pass
            elif i == len(p) - 1 and ord(p[i - 1]) - 97 == (ord(p[i]) - 1 - 97) % 26:
                pass
            else:
                res |= set([p[s:i+1][x:y] for x, y in itertools.combinations(range(len(p[s:i+1])+1), r=2)])
                s = i + 1
            i += 1
        res |= set([p[s:i][x:y] for x, y in itertools.combinations(range(len(p[s:i]) + 1), r=2)])
        return len(res)

# 我们看abcd这个字符串，以d结尾的子字符串有abcd, bcd, cd, d，那么我们可以发现bcd或者cd这些以d结尾的字符串的子字符串都包含在abcd中，那么我们知道以某个字符结束的最大字符串包含其他以该字符结束的字符串的所有子字符串. 那么题目就可以转换为分别求出以每个字符(a-z)为结束字符的最长连续字符串就行了.
import collections
class Solution(object):
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        pattern = 'abcdefghijklmnopqrstuvwxyza'
        cmap = collections.defaultdict(int)
        cur_len = 0
        for i in range(len(p)):
            if i and p[i-1:i+1] not in pattern:
                cur_len = 1
            else:
                cur_len += 1
            cmap[p[i]] = max(cur_len, cmap[p[i]])
        return sum(cmap.values())
