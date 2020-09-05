from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = []

        for i in range(numRows):
            output.append([1])
            for j in range(1, i):
                output[i].append(output[i-1][j] + output[i-1][j-1])
            if i != 0:
                output[i].append(1)
        
        return output


sol = Solution()
print(sol.generate(1))