# Lexicographical Numbers

"""
Given an integer n, return 1 - n in lexicographical order.

For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].

Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000.
"""

class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
      	if n < 10:
            return list(range(1, n+1))
        res = list(range(1, 10))
        for i in range(1, int(n / 10)):
            index = res.index(i) + 1
            res[index:index] = list(range(i*10, (i+1)*10))
        index = res.index(int(n/10)) + 1
        res[index:index] = list(range(int(n/10)*10, n+1))
