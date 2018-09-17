# Longest Palindrome

"""
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = {}
        for c in s:
            cnt[c] = 1 if c not in cnt else cnt[c] + 1
        l = 0
        for c in cnt:
            if cnt[c] % 2 == 0:
                l += cnt[c]
                cnt[c] = 0
            elif cnt[c] > 1:
                l += cnt[c] - 1
                cnt[c] = 1
        for c in cnt:
            if cnt[c] == 1:
                l += 1
                break
        return l
