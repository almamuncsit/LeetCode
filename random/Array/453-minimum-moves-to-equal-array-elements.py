from typing import List


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        sum = 0
        m = min(nums)
        i = nums.index(m)
        for j in range(len(nums)):
            if i != j:
                sum += nums[j] - nums[i]

        return sum


sol = Solution()
numbers = [1, 2, 3]
print(sol.minMoves(numbers))
