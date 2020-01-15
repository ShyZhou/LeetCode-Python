# Integer to English Words

# Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 2^31 - 1.

# Example 1:
# Input: 123
# Output: "One Hundred Twenty Three"

# Example 2:
# Input: 12345
# Output: "Twelve Thousand Three Hundred Forty Five"

# Example 3:
# Input: 1234567
# Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

# Example 4:
# Input: 1234567891
# Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"

class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()

        def words(n):
            if n < 20:
                return to19[n-1: n]
            if n < 100:
                return [tens[n / 10 - 2]] + words(n % 10)
            if n < 1000:
                return [to19[n/100 - 1]] + ['Hundred'] + words(n % 100)
            for p, w in enumerate(('Thousand', 'Million', 'Billion'), 1):
                if n < 1000 ** (p + 1):
                    return words(n / 1000 ** p) + [w] + words (n % 1000 ** p)

        return ' '.join(words(num)) or 'Zero'
