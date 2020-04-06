from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        non_zero_pointer = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero_pointer] = nums[i]
                non_zero_pointer += 1
        while non_zero_pointer < len(nums):
            nums[non_zero_pointer] = 0
            non_zero_pointer += 1


# sol = Solution()
# n = [0, 1, 7, 0, 3, 12]
# print(sol.moveZeroes(n))
