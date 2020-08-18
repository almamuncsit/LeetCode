class Solution:
    def maximum69Number(self, num):
        num_str = list(str(num))
        changeable = False
        for x in range(len(num_str)):
            if not changeable and num_str[x] == '6':
                num_str[x] = '9'
                changeable = True

        return int(''.join(num_str))


sol = Solution()
print(sol.maximum69Number(9669))
