from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        current_sum = 0
        for x in nums:
            current_sum += x
            if current_sum > max_sum:
                max_sum = current_sum
            if current_sum < 0:
                current_sum = 0

        return max_sum


sol = Solution()
n = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(sol.maxSubArray(n))
