from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        look_up = {}
        for num in arr:
            if num * 2 in look_up or num / 2 in look_up:
                return True
            look_up[num] = 1
        return False
