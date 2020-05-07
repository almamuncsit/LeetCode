from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        i = 0
        while i < len(arr)-1:
            if arr[i] == 0:
                arr.insert(i + 1, 0)
                arr.pop()
                i += 1
            i += 1
        print(arr)


sol = Solution()
sol.duplicateZeros([1, 2, 3])
