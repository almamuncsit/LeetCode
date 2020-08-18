from typing import List


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        def square(x):
            return x ** 2

        square_a = list(map(square, A))
        square_a.sort()
        return square_a
