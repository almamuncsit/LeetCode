# class Solution:
#     def isPowerOfTwo(self, n: int) -> bool:
#         if n <= 0:
#             return False
#         while n > 1:
#             if n % 2 != 0:
#                 return False
#             else:
#                 n = n//2

#         return True

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        binary = bin(n)[2:]
        if binary[0] == 0:
            return False
        for i in range(1, len(binary)):
            if binary[i] != '0':
                return False
        
        return True


sol = Solution()
print(sol.isPowerOfTwo(-16))
