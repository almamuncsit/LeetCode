from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 1
        if nums[i] != nums[j]:
            nums[i + 1] = nums[j]
            i += 1
        j += 1
        return i


sol = Solution()
print(sol.removeDuplicates([1, 1, 2]))
