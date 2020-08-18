from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 2:
            return True
        x1, y1, x2, y2 = coordinates[0][0], coordinates[0][1], coordinates[1][0], coordinates[1][1]
        for i in range(2, len(coordinates)):
            x = coordinates[i][0]
            y = coordinates[i][1]
            if (y - y1) * (x2 - x1) != (x - x1) * (y2 - y1):
                return False

        return True
