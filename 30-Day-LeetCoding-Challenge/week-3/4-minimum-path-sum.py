from typing import List


class Solution:
    def __init__(self):
        self.look_up = []

    def findMinimum(self, grid, i, j):
        if i >= len(grid) or j >= len(grid[0]):
            return None
        if self.look_up[i][j]:
            return self.look_up[i][j]

        bottom_total = self.findMinimum(grid, i + 1, j)
        right_total = self.findMinimum(grid, i, j + 1)

        min_val = 0
        if bottom_total is not None and right_total is not None:
            min_val = min(bottom_total, right_total)
        elif bottom_total:
            min_val = bottom_total
        elif right_total:
            min_val = right_total
        self.look_up[i][j] = min_val + grid[i][j]
        return self.look_up[i][j]

    def minPathSum(self, grid: List[List[int]]) -> int:
        self.look_up = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        return self.findMinimum(grid, 0, 0)


grids = [[9, 9, 0, 8, 9, 0, 5, 7, 2, 2, 7, 0, 8, 0, 2, 4, 8],
         [4, 4, 2, 7, 6, 0, 9, 7, 3, 2, 5, 4, 6, 5, 4, 8, 7],
         [4, 9, 7, 0, 7, 9, 2, 4, 0, 2, 4, 4, 6, 2, 8, 0, 7],
         [7, 7, 9, 6, 6, 4, 8, 4, 8, 7, 9, 4, 7, 6, 9, 6, 5],
         [1, 3, 7, 5, 7, 9, 7, 3, 3, 3, 8, 3, 6, 5, 0, 3, 6],
         [7, 1, 0, 7, 5, 0, 6, 6, 5, 3, 2, 6, 0, 0, 9, 5, 7],
         [6, 5, 6, 3, 8, 1, 8, 6, 4, 4, 3, 4, 9, 9, 3, 3, 1],
         [1, 0, 2, 9, 7, 9, 3, 1, 7, 5, 1, 8, 2, 8, 4, 7, 6],
         [9, 6, 7, 7, 4, 1, 4, 0, 6, 5, 1, 9, 0, 3, 2, 1, 7],
         [2, 0, 8, 7, 1, 7, 4, 3, 5, 6, 1, 9, 4, 0, 0, 2, 7],
         [9, 8, 1, 3, 8, 7, 1, 2, 8, 3, 7, 3, 4, 6, 7, 6, 6],
         [4, 8, 3, 8, 1, 0, 4, 4, 1, 0, 4, 1, 4, 4, 0, 3, 5],
         [6, 3, 4, 7, 5, 4, 2, 2, 7, 9, 8, 4, 5, 6, 0, 3, 9],
         [0, 4, 9, 7, 1, 0, 7, 7, 3, 2, 1, 4, 7, 6, 0, 0, 0]]

sol = Solution()
print(sol.minPathSum(grids))
