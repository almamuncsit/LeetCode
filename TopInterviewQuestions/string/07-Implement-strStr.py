class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        
        needle_len = len(needle)
        for x in range(len(haystack) - needle_len+1):
            if haystack[x:x + needle_len] == needle:
                return x
        
        return -1


haystack = "aaaaa"
needle = "bba"
sol = Solution()
print(sol.strStr(haystack, needle))
