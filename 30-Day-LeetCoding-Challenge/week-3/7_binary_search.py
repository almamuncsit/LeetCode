# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
# class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:

    def binary_search(self, arr):
        left = 0
        right = len(arr) - 1
        if arr[0] == 1:
            return 0
        if arr[-1] == 0:
            return -1

        while left < right:
            mid = (left + right) // 2
            if arr[mid] == 1 and arr[mid - 1] == 0:
                return mid
            elif arr == 1:
                right = mid - 1
            elif arr[mid + 1] == 1:
                return mid + 1
            else:
                left = mid + 1

    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        # mat = binaryMatrix.dimensions()
        n, m = len(binaryMatrix), len(binaryMatrix[0])
        min_start = -1
        for i in range(n):
            start = self.binary_search(binaryMatrix[i])
            if min_start == -1:
                min_start = start
            elif start != -1 and start < min_start:
                min_start = start
        return min_start


matrix = [[1, 1, 1, 1, 1], [0, 0, 0, 1, 1], [0, 0, 1, 1, 1], [0, 0, 0, 0, 1], [0, 0, 0, 0, 0]]
sol = Solution()
print(sol.leftMostColumnWithOne(matrix))
