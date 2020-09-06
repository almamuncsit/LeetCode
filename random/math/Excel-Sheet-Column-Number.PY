class Solution:
    def titleToNumber(self, s: str) -> int:
        s_reversed = s[::-1]
        number = 0
        for i in range(len(s_reversed)):
            number_of_char = (ord(s_reversed[i]) - ord('A') ) + 1
            number += number_of_char * 26 ** i
        
        return number


sol = Solution()
print(sol.titleToNumber("AB"))