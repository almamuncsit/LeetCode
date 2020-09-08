from collections import Counter


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_count = {}
        t_count = {}

        for value in Counter(s).values():
            s_count[value] = s_count.get(value, 0) + 1
        
        for value in Counter(t).values():
            t_count[value] = t_count.get(value, 0) + 1

        if s_count == t_count:
            return True

        return False


sol = Solution()
s = "eggg"
t = "add"
print(sol.isIsomorphic(s, t))
