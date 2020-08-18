from typing import List
import heapq


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        heapq._heapify_max(nums)
        if len(nums) > 2:
            heapq._heappop_max(nums)
            heapq._heappop_max(nums)
        return heapq._heappop_max(nums)


sol = Solution()
nums = [5, 5, 6, 3, 12, 3, 2, 1]
print(sol.thirdMax(nums))
