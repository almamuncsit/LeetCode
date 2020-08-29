class Solution:
    def isPalindrome(self, s: str) -> bool:
        char_str = [c.lower() for c in s if c.isalnum()]

        return char_str == list(reversed(char_str))


sol = Solution()
s = "0P"
print(sol.isPalindrome(s))
