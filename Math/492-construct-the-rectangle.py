from typing import List
import math


class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        sqrt = int(math.sqrt(area))
        for i in range(sqrt, 0, -1):
            if area % i == 0:
                return [int(area/i), i]

        return [sqrt]


sol = Solution()
print(sol.constructRectangle(122122))
