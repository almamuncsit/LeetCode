from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        memo = {}

        for i, num in enumerate(nums):
            if num in memo and (i-memo[num]) <= k:
                return True
            else:
                memo[num] = i

        return False
