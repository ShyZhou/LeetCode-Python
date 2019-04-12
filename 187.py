# Repeated DNA Sequences

"""
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

Example:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

Output: ["AAAAACCCCC", "CCCCCAAAAA"]
"""

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        cur = s[0:10]
        dna_dict = {cur: 1}
        for i in range(10, len(s)):
            cur = cur[1:] + s[i]
            if cur in dna_dict:
                dna_dict[cur] += 1
            else:
                dna_dict[cur] = 1
        return [k for k in dna_dict if dna_dict[k] > 1]
