from collections import Counter


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_count = {}
        t_count = {}

        for i in range(len(s)):
            if (s[i] in s_count and s_count[s[i]] != t[i]) or (t[i] in t_count and t_count[t[i]] != s[i]):
                return False

            s_count[s[i]] = t[i]
            t_count[t[i]] = s[i]

        return True


sol = Solution()
s = "egg"
t = "add"
print(sol.isIsomorphic(s, t))
