# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         i, j = 0, 0
#         while i < len(s) and j < len(t):
#             if s[i] == t[j]:
#                 i += 1
#                 j += 1
#             else:
#                 j += 1
        
#         return i == len(s)


# Dynamic Programming Solution
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        def lcs(X, Y):
            m = len(X)
            n = len(Y)
            matrix = [ [None] * (n+1) for i in range(m+1) ]

            for i in range(m+1):
                for j in range(n+1):
                    if i == 0 or j == 0:
                        matrix[i][j] = 0
                    elif X[i-1] == Y[j-1]:
                        matrix[i][j] = matrix[i-1][j-1] + 1
                    else:
                        matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])
                    
                    if matrix[i][j] == len(s):
                        return matrix[i][j]
            
            return matrix[m][n]

        return lcs(s, t) == len(s)


sol = Solution()
s = "abc"
t = "ahbgdc"
print(sol.isSubsequence(s, t))
