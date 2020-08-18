from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_one = 0
        current_one = 0
        for num in nums:
            if num == 1:
                current_one += 1
            else:
                current_one = 0
            print(max_one, current_one)
            if current_one > max_one:
                max_one = current_one

        return max_one


sol = Solution()
print(sol.findMaxConsecutiveOnes([1, 1, 0, 1]))
