from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        length = len(nums)
        i = 0
        while i < length:
            if i == length - 1:
                return nums[i]
            if nums[i] != nums[i + 1]:
                return nums[i]
            i += 2
