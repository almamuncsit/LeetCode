from typing import List


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        new_arr = []
        for item in A:
            if item % 2 == 0:
                new_arr.append(item)
        for item in A:
            if item % 2 != 0:
                new_arr.append(item)
        return new_arr


sol = Solution()
print(sol.sortArrayByParity([3, 1, 2, 4]))
