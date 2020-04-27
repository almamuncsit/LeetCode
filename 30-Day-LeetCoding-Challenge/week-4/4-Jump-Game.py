from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = [False] * len(nums)
        memo[-1] = True
        last_true = len(memo) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= last_true:
                memo[i] = True
                last_true = i
        return memo[0]

    # def canJump(self, nums: List[int]) -> bool:
    #     memo = [False] * len(nums)
    #     memo[-1] = True
    #     for i in range(len(nums) - 2, -1, -1):
    #         for j in range(i + 1, i + nums[i] + 1):
    #             if memo[j]:
    #                 memo[i] = True
    #                 break
    #     return memo[0]


sol = Solution()
arr = [3, 2, 1, 0, 4]
print(sol.canJump(arr))
