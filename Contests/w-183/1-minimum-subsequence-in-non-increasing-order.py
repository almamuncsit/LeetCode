from typing import List


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort( reverse=True )
        total = sum(nums)
        sub_total = 0
        sub_array = []
        for num in nums:
            sub_total += num
            sub_array.append(num)
            if sub_total > total - sub_total:
                break

        return sub_array


sol = Solution()
nums = [6]
print(sol.minSubsequence(nums))
