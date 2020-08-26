from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_counter = Counter(s)
        for i in range(len(s)):
            if s_counter[s[i]] == 1:
                return i
        return -1
