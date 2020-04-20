from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[left] < nums[mid] and nums[left] <= target < nums[mid]:
                right = mid - 1
            elif nums[right] > nums[mid] and nums[right] >= target > nums[mid]:
                left = mid + 1
            elif nums[left] > nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        return -1


sol = Solution()
nums = [4, 5, 6, 7, 0, 1, 2]
print(sol.search(nums, 1))
