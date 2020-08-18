class Solution:
    def plusOne(self, digits):
        n = len(digits) - 1
        number = 1
        while n > -1:
            if digits[n] == 9:
                digits[n] = 0
                n -= 1
            else:
                digits[n] += 1
                return digits

        if n == -1:
            digits.insert(0, 1)
            return digits


arr = [9, 9, 9]
sol = Solution()
print(sol.plusOne(arr))
