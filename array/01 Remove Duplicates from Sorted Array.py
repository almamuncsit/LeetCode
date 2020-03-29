# Remove Duplicates from Sorted Array
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        b = sorted(list(set(nums)))
        nums[0:len(b)] = b[0:len(b)]
        return len(b)
