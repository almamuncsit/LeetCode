class Solution:
    def fib(self, N: int) -> int:
        first, second = 0, 1
        if N == 0:
            return first
        if N == 1:
            return 1

        for i in range(2, N+1):
            total = first + second
            first, second = second, total

        return second


sol = Solution()
print(sol.fib(10))