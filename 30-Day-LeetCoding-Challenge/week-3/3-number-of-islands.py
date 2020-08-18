from typing import List


class Solution:
    def bfs(self, grid, i, j):
        stack = [(i, j)]
        while stack:
            i, j = stack.pop()
            grid[i][j] = 0
            if j + 1 < len(grid[i]) and grid[i][j + 1] == '1':
                stack.append((i, j + 1))
            if j - 1 >= 0 and grid[i][j - 1] == '1':
                stack.append((i, j - 1))
            if i + 1 < len(grid) and grid[i+1][j] == '1':
                stack.append((i+1, j))
            if i - 1 >= 0 and grid[i-1][j] == '1':
                stack.append((i-1, j))

    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    islands += 1
                    self.bfs(grid, i, j)
        return islands


grids = [['1', '1', '0', '0', '0'],
         ['1', '1', '0', '0', '0'],
         ['0', '0', '1', '0', '0'],
         ['0', '0', '0', '1', '1']]
sol = Solution()
print(sol.numIslands(grids))
