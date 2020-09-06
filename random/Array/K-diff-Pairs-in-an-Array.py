from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        total_pair = 0
        used = {}
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i], nums[j]) in used or (nums[j], nums[i]) in used:
                    continue
                if abs(nums[i] - nums[j]) == k:
                    total_pair += 1
                    used[(nums[i], nums[j])] = 1
                    used[(nums[j], nums[i])] = 1
        
        return total_pair


sol = Solution()
nums = [1, 3, 1, 5, 4]
k = 0
print(sol.findPairs(nums, k))
