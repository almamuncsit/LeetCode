class Solution:
    def romanToInt(self, s: str) -> int:
        romans = { "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000 }

        str_reverse_list = list(reversed(s))
        last_value = 1
        output = 0
        for key in str_reverse_list:
            if romans[key] >= last_value:
                output += romans[key]
            else:
                output -= romans[key]
            
            last_value = romans[key]

        return output
        

sol = Solution()
print(sol.romanToInt("MCMXCIV"));
