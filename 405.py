# Convert a Number to Hexadecimal

"""
Given an integer, write an algorithm to convert it to hexadecimal. For negative integer, two’s complement method is used.

Note:

All letters in hexadecimal (a-f) must be in lowercase.
The hexadecimal string must not contain extra leading 0s. If the number is zero, it is represented by a single zero character '0'; otherwise, the first character in the hexadecimal string will not be the zero character.
The given number is guaranteed to fit within the range of a 32-bit signed integer.
You must not use any method provided by the library which converts/formats the number to hex directly.

Example 1:

Input:
26

Output:
"1a"

Example 2:

Input:
-1

Output:
"ffffffff"
"""

class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num < 0:
            num += 2**32
        n_to_hex = {
            0: '0',
            1: '1',
            2: '2',
            3: '3',
            4: '4',
            5: '5',
            6: '6',
            7: '7',
            8: '8',
            9: '9',
            10: 'a',
            11: 'b',
            12: 'c',
            13: 'd',
            14: 'e',
            15: 'f'
        }
        h = ''
        while num > 15:
            h = n_to_hex[num % 16] + h
            num = num / 16
        h = n_to_hex[num] + h
        return h
