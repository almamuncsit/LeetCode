from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        negativeNumber = 0
        for items in grid:
            for item in items:
                if item < 0:
                    negativeNumber += 1

        return negativeNumber


grid = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
sol = Solution()
sol.countNegatives(grid)
