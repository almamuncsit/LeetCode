from collections import Counter


class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        str_arr = str.split()
        pattern_count = {}
        str_count = {}
        if len(pattern) != len(str_arr):
            return False
        
        for char, word in zip(pattern, str_arr):
            if (char in pattern_count and pattern_count[char] != word) or (word in str_count and str_count[word] != char):
                return False
            str_count[word] = char
            pattern_count[char] = word
        
        return True

sol = Solution()
pattern = "abbac"
str = "dog cat cat dog"
print(sol.wordPattern(pattern, str))
