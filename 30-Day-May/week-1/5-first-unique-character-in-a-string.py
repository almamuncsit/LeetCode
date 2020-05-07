from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_counter = Counter(s)
        print(s_counter)
        for i in range(len(s)):
            if s_counter[s[i]] == 1:
                return i
        return -1


sol = Solution()
print(sol.firstUniqChar("loveleetcode"))
