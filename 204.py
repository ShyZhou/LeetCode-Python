# Count Primes

"""
Count the number of prime numbers less than a non-negative number, n.
"""

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """

        """
        Sieve of Eratosthenes: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
        """

        if n <= 2:
            return 0
        A = [True] * n
        for i in range(2, int(n ** 0.5) + 1):
            if A[i]:
                j = 2
                while j * i < n:
                    A[j * i] = False
                    j += 1
        res = 0
        for i in range(2, n):
            if A[i]:
                res += 1
        return res