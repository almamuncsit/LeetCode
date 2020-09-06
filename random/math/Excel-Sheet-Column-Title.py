import string

class Solution:
    def convertToTitle(self, n: int) -> str:
        column = ''
        chars = string.ascii_uppercase
        
        while n > 0:
            n -= 1
            column = chars[n%26] + column
            n //= 26
        
        return column


sol = Solution()
print(sol.convertToTitle(701))
