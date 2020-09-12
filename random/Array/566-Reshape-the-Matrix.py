from typing import List

class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(nums) * len(nums[0]) != r * c:
            return nums
        
        matrix = []
        y = 0
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                if y == 0:
                    matrix.append([ nums[i][j] ])
                else:
                    matrix[-1].append(nums[i][j])
                y += 1
                y %= c

        return matrix 


sol = Solution()
nums = [[1, 2, 5, 4],
 [3, 4, 8, 4]]
r = 4
c = 2
print(sol.matrixReshape(nums, r, c))
