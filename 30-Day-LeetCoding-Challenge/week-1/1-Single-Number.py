from typing import List


class Solution:

    def singleNumber(self, nums: List[int]) -> int:
        xor_sum = 0
        for x in nums:
            xor_sum ^= x

        return xor_sum


numbers = [4, 1, 2, 1, 2]
sol = Solution()
print(sol.singleNumber(numbers))
