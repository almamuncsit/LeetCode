from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1 for _ in nums]
        left_pointer = 1
        right_pointer = 1
        for i in range(len(nums)):
            answer[i] *= left_pointer
            left_pointer *= nums[i]
            answer[-1 - i] *= right_pointer
            right_pointer *= nums[-1 - i]
        return answer


sol = Solution()
numbers = [1, 2, 3, 4]
print(sol.productExceptSelf(numbers))
