from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        map = {0: -1}
        maxlen, count = 0, 0
        for i in range(len(nums)):
            count = count + (1 if nums[i] == 1 else -1)
            if count in map:
                maxlen = max(maxlen, i - map[count])
            else:
                map[count] = i

        return maxlen


sol = Solution()
numbers = [0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0]
print(sol.findMaxLength(numbers))
