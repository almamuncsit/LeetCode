from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        max_target = max(target)
        arr = []
        for i in range(1, max_target+1):
            if i in target:
                arr.append('Push')
            else:
                arr.append('Push')
                arr.append('Pop')
        return arr


sol = Solution()
print(sol.buildArray([2,3,4], 4))
