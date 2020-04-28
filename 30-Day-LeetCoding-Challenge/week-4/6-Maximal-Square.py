from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix:
            return 0
        n, m = len(matrix), len(matrix[0])
        memo = [[0 for _ in range(m)] for __ in range(n)]
        max_square = 0
        for i in range(n):
            for j in range(m):
                memo[i][j] = min(memo[i - 1][j - 1], memo[i - 1][j], memo[i][j - 1]) + 1 if matrix[i][j] == '1' else 0
                max_square = max(max_square, memo[i][j])
        return max_square ** 2


sol = Solution()
mat = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
print(sol.maximalSquare(mat))
