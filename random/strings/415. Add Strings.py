class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        new_num1 = list(reversed(num1))
        new_num2 = list(reversed(num2))
        length = max(len(new_num1), len(new_num2))
        carry = 0
        ans = []
        for i in range(length):
            total = carry
            if i < len(new_num1):
                total += int(new_num1[i])
            if i < len(new_num2):
                total += int(new_num2[i])

            ans.append(str(total % 10))
            carry = total//10
        if carry:
            ans.append(str(carry))

        return ''.join(reversed(ans))


sol = Solution()
num_1 = "23452345"
num_2 = "92423"
print(sol.addStrings(num_1, num_2))
