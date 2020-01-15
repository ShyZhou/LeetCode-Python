# Minimum Window Substring

# Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

# Example:

# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"
# Note:

# If there is no such window in S that covers all characters in T, return the empty string "".
# If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

import collections
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ''

        dict_t = collections.Counter(t)
        # Number of unique characters in t, which need to be present in the desired window.
        required = len(dict_t)

        l, r = 0, 0

        # formed is used to keep track of how many unique characters in t are present in the current window in its desired frequency.
        formed = 0

        # Dictionary which keeps a count of all the unique characters in the current window.
        window_counts = collections.defaultdict(int)

        res = (float('inf'), None, None)

        while r < len(s):
            # Add one character from the right to the window
            character = s[r]
            window_counts[character] += 1

            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1

            # Try and contract the window till the point where it ceases to be 'desirable'.
            while l <= r and formed == required:
                character = s[l]

                if r - l + 1 < res[0]:
                    res = (r - l + 1, l, r)

                # The character at the position pointed by the `left` pointer is no longer a part of the window.
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1

                l += 1

            r += 1
        return '' if res[0] == float('inf') else s[res[1]: res[2] + 1]
