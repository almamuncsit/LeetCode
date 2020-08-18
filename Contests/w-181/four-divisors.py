import math
from typing import List


class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        divisiors = {}
        total = 0
        for num in nums:
            divisiors[num] = [1, num]
            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    divisiors[num].append(i)
                    divisiors[num].append((num // i))

        for num in nums:
            div = list(set(divisiors[num]))
            if len(div) == 4:
                total += sum(div)

        return total


sol = Solution()
nums = [21, 21]
print(sol.sumFourDivisors(nums))
