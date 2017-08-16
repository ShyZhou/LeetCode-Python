# Keyboard Row

"""
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.


American keyboard


Example 1:
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
Note:
You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.
"""

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        dict = {
            1 : ('z', 'x', 'c', 'v', 'b', 'n', 'm'),
            2 : ('a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'),
            3 : ('q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p')
        }
        good_words = []
        for word in words:
            target_row = 0
            in_row = 0
            bad_word = 0
            for char in word:
                for key, value in dict.items():
                    if char.lower() in value:
                        in_row = key
                        break
                if target_row != 0 and target_row != in_row:
                    bad_word = 1
                    break
                if target_row == 0:
                    target_row = in_row
            if bad_word == 1:
                continue
            good_words.append(word)
        return good_words