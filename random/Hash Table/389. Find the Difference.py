from collections import Counter


# Solution hash map
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if not s:
            return t
        
        new_str = s + t
        xorResult = ord(new_str[0])
        
        for i in range(1, len(new_str)):
            xorResult ^= ord(new_str[i])

        return chr(xorResult)

# Solution Using Hash Map
# class Solution:
#     def findTheDifference(self, s: str, t: str) -> str:
#         s_count = Counter(s)
#         t_count = Counter(t)

#         for key, value in t_count.items():
#             if key not in s_count or s_count[key] < value:
#                 return key


sol = Solution()
print(sol.findTheDifference('abcd', 'abcde'))