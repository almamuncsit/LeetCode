class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 0:
            return False

        while n >= 3:
            if n % 3 != 0:
                return False
            n = n // 3

        if n == 1:
            return True
