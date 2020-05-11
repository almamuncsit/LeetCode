from typing import List
from collections import defaultdict


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        trusted = defaultdict(list)
        trusted_by = defaultdict(list)
        for item in trust:
            trusted[item[0]].append(item[1])
            trusted_by[item[1]].append(item[0])

        for i in range(1, N+1):
            if i not in trusted_by:
                trusted_by[i] = []

        for item in trusted_by.items():
            if len(item[1]) == N - 1 and item[0] not in trusted and item[0] not in item[1]:
                return item[0]

        return -1

    # def findJudge(self, N: int, trust: List[List[int]]) -> int:
    #     trusts = [0] * (N + 1)
    #     for (a, b) in trust:
    #         trusts[a] -= 1
    #         trusts[b] += 1
    #
    #     for i in range(1, len(trusts)):
    #         if trusts[i] == N - 1:
    #             return i
    #     return -1


sol = Solution()
print(sol.findJudge(1, []))
