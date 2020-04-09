class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        final_s = []
        final_t = []
        for c in S:
            if c == '#':
                if final_s:
                    final_s.pop()
            else:
                final_s.append(c)
        for c in T:
            if c == '#':
                if final_t:
                    final_t.pop()
            else:
                final_t.append(c)
        return final_s == final_t


sol = Solution()
S = "ab#c"
T = "ad#c"
print(sol.backspaceCompare(S, T))
