from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum_of_nums = sum(nums)
        n = len(nums)
        sum_series = (n * (n+1)) // 2

        return sum_series - sum_of_nums


sol = Solution()
numbers = [9, 6, 4, 2, 3, 5, 7, 0, 1]
print(sol.missingNumber(numbers))
