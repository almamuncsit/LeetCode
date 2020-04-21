# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
# class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:


class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        mat = binaryMatrix.dimensions()
        n, m = mat[0], mat[1]
        i, j = 0, m - 1
        while i < n and j > -1:
            if binaryMatrix.get(i, j) == 1:
                j -= 1
            else:
                i += 1
        if j == m-1:
            return -1
        else:
            return j + 1


matrix = [
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 0, 1]
]

# sol = Solution()
# print(sol.leftMostColumnWithOne(matrix))
