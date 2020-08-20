from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited_nums = {}
        for i in range(len(nums)):
            need = target-nums[i]
            if need in visited_nums:
                return [visited_nums[need], i]
            else:
                visited_nums[nums[i]] = i


sol = Solution()
nums = [2, 7, 11, 15]
target = 9
disappeared = sol.twoSum(nums, target)
print(disappeared)
