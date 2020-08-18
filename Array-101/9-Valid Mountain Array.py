from typing import List


class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        n = len(A)
        i = 0
        while i + 1 < n and A[i + 1] > A[i]:
            i += 1
        if i == 0 or i == n - 1:
            return False
        while i + 1 < n and A[i + 1] < A[i]:
            i += 1
        return i == n - 1
