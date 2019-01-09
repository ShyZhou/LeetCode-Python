# Repeated Substring Pattern

"""
Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

Example 1:

Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.

Example 2:

Input: "aba"
Output: False

Example 3:

Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
"""

# 从原字符串长度的一半遍历到1，如果当前长度能被总长度整除，说明可以分成若干个子字符串，我们将这些子字符串拼接起来看跟原字符串是否相等
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s or len(s) < 2:
            return False

        strlen = len(s)
        pos = strlen / 2
        while pos > 0:
            if strlen % pos == 0:
                substr = s[:pos]
                if substr * (strlen / pos) == s:
                    return True
            pos -= 1
        return False

# Use regular expression
import re
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return bool(re.match(r"^([a-z]+)\1+$", s))

# 输入字符串的第一个字符串是重复子字符串的第一个字符
# 输入字符串的最后一个字符串是重复子字符串的最后一个字符
# 令S1 = S + S（其中输入字符串中的S）
# 删除S1的第一个和最后一个字符，生成字符串S2。
# 如果S存在于S2中，则返回true否则为false。

# 这个思想的精髓就在于通过拷贝一次字符串，并且各自破坏一小部分，然后通过两个串的拼接完成原串的查找。如果串不满足要求的特性，是拼装不出来的。
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return False

        ss = (s + s)[1:-1]
        return ss.find(s) != -1
