from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        number_of_sum, total = 0, 0
        dic = {0: 1}
        for i in range(len(nums)):
            total += nums[i]
            if total - k in dic:
                number_of_sum += dic[total - k]
            dic[total] = dic.get(total, 0) + 1
        return number_of_sum


nums = [0, 0, 0, 0, 0, 0, 0, 0]
k = 0
sol = Solution()
print(sol.subarraySum(nums, k))
