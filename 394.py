# Decode String

"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:
s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
"""

# Use Stack, 2 stacks, use defaultdict for stack
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        k = 1
        parts = collections.defaultdict(str)
        digits = collections.defaultdict(int)
        for c in s:
            if c.isdigit():
                digits[k] = digits[k] * 10 + int(c)
            elif c == '[':
                k += 1
            elif c == ']':
                parts[k - 1] += digits[k - 1] * parts[k]
                digits[k - 1] = 0
                parts[k] = ''
                k -= 1
            else:
                parts[k] += c
        return parts[1]
