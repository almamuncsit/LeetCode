from collections import Counter
from typing import List


class Solution:
    def countElements(self, arr: List[int]) -> int:
        total_count = 0
        data = Counter(arr)
        for item in data.items():
            if item[0] + 1 in data:
                total_count += item[1]
        return total_count


sol = Solution()
ar = [1, 3, 2, 3, 5, 0]
print(sol.countElements(ar))
