from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        memo = {}
        for i in range(len(numbers)):
            need = target - numbers[i]
            if need in memo:
                return [memo[need], i+1]
            else:
                memo[numbers[i]] = i+1


sol = Solution()
numbers = [2, 7, 11, 15]
target = 9
print(sol.twoSum(numbers, target))