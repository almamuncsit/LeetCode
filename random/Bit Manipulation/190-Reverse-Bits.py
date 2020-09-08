class Solution:
    def reverseBits(self, n: int) -> int:
        binary = bin(n)[2:]
        binary = binary[::-1] + "0" * int(32-len(binary))

        return int(binary, 2)


sol = Solution()
print(sol.reverseBits(43261596))
