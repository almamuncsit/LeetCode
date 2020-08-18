from typing import List


class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        P = [x for x in range(1, m + 1)]
        output = []
        for q in queries:
            index = P.index(q)
            output.append(index)
            temp_data = P[index]
            del P[index]
            P.insert(0, temp_data)
        return output


sol = Solution()
queries = [7,5,5,8,3]
m = 8
print(sol.processQueries(queries, m))
