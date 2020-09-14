from typing import List
import math


class Solution:

    def get_val(self, i: int, j: int, M: List[List[int]]) -> bool:
        return (i >= 0 and i <len(M)) and (j >= 0 and j < len(M[0]))

    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        matrix = [[0] * len(M[0]) for _ in range(len(M))]
        
        for i in range(len(M)):
            for j in range(len(M[0])):
                count = 1
                total = M[i][j]

                pairs = [
                    (i-1, j-1), (i-1, j), (i-1, j+1),
                    (i+1, j-1), (i+1, j), (i+1, j+1),
                    (i, j-1), (i, j+1)
                ]
                for p, q in pairs:
                    if self.get_val(p, q, M):
                        count += 1
                        total += M[p][q]
                
                matrix[i][j] = math.floor(total/count)

        return matrix



sol = Solution()
m = [[1, 1, 1],
     [1, 0, 1],
     [1, 1, 1]]
print(sol.imageSmoother(m))
