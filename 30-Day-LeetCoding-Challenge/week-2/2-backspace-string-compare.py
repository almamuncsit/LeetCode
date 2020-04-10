class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        final_s = []
        final_t = []
        for c in S:
            if c != '#':
                final_s.append(c)
            elif final_s:
                final_s.pop()
        for c in T:
            if c != '#':
                final_t.append(c)
            elif final_t:
                final_t.pop()
        return final_s == final_t


sol = Solution()
S = "ab#c"
T = "ad#c"
print(sol.backspaceCompare(S, T))
