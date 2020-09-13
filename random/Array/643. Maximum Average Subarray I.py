from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) < k:
            return None
        
        total = sum(nums[0:k])
        max_avg = total/k
        
        for i in range(k, len(nums)):
            total = total + nums[i] - nums[i-k]
            max_avg = max(max_avg, total / k)
        
        return max_avg


sol = Solution()
nums = [1, 12, -5, -6, 50, 3]
k = 4
print(sol.findMaxAverage(nums, k))
