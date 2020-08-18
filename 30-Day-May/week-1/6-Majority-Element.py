from typing import List
from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        for item in counter.items():
            if item[1] > (len(nums) // 2):
                return item[0]


sol = Solution()
print(sol.majorityElement([3, 2, 3]))
