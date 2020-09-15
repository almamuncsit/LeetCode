import math

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and math.log(num, 4).is_integer()

sol = Solution()
print(sol.isPowerOfFour(13))


# class Solution:
#     def isPowerOfFour(self, num: int) -> bool:
#         if num < 0:
#             return False

#         while num >= 4:
#             if num % 4 != 0:
#                 return False
#             num = num // 4

#         if num == 1:
#             return True
