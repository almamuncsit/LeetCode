class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        for key, val in roman.items():
            s = s.replace(key, str(val) + ' ')
        
        return sum(list(map(int, s.split())))
        

sol = Solution()
print(sol.romanToInt("MCMXCIV"));
