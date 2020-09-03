from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0

        low, high = 0, len(nums)-1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high -= 1
            else:
                low += 1
        
        return mid + 1 if nums[mid] < target else mid


sol = Solution()
nums = [1, 3, 5, 6]
print(sol.searchInsert(nums, 0))