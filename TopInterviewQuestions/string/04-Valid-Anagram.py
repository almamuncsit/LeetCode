# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if sorted(s) == sorted(t):
#             return True
#         else:
#             return False

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = Counter(s)
        t_count = Counter(t)

        for char, count in t_count.items():
            if char in s_count:
                s_count[char] -= count
            else:
                return False

        for count in s_count.values():
            if count != 0:
                return False
        
        return True


sol = Solution()
s = "anagram"
t = "nagaram"
print(sol.isAnagram(s, t))
