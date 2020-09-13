from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        nums.sort()
        first_product = nums[-1] * nums[-2] * nums[-3]
        second_product = nums[-1] * nums[0] * nums[1]
        
        return max(first_product, second_product)


sol = Solution()
nums = [1, 2, 3, 4]
print(sol.maximumProduct(nums))
