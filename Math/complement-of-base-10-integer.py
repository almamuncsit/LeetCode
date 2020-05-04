class Solution:
    def findComplement(self, N: int) -> int:
        all_one = (2 ** len(bin(N)[2:])) - 1

        return all_one ^ N


sol = Solution()
print(sol.findComplement(5))
