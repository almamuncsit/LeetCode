import math


class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        primes = [1]*n
        primes[0], primes[1] = 0, 0

        for i in range(2, int(math.sqrt(n))+1):
            for j in range(i*i, n, i):
                primes[j] = 0

        return primes.count(1)


sol = Solution()
print(sol.countPrimes(16))
