from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        if not s:
            return 0

        counter = Counter(list(s))
        length = 0

        for item in counter.items():
            length += (counter[item[0]] // 2) * 2
            counter[item[0]] %= 2

        if sum(counter.values()) > 0:
            length += 1

        return length


sol = Solution()
msg = "bb"
print(sol.longestPalindrome(msg))
