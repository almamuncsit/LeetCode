from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = sorted(heights)
        move = 0
        for i in range(len(heights)):
            if sorted_heights[i] != heights[i]:
                move += 1
        return move
