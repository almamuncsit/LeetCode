class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        text1 = '0' + text1
        text2 = '0' + text2
        matrix = [[0 for _ in range(len(text1))] for i in range(len(text2))]
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if text2[i] == text1[j]:
                    matrix[i][j] = matrix[i - 1][j - 1] + 1
                else:
                    matrix[i][j] = max(matrix[i][j - 1], matrix[i - 1][j])
        return matrix[-1][-1]


sol = Solution()
text1 = "abcde"
text2 = "ace"
print(sol.longestCommonSubsequence(text1, text2))
