# class Solution:
#     def findComplement(self, N: int) -> int:
#         all_one = (2 ** len(bin(N)[2:])) - 1
#
#         return all_one ^ N


class Solution:
    def findComplement(self, num: int) -> int:
        binary = str(bin(num)[2:])
        complement = ''
        for b in binary:
            if b == '1':
                complement += '0'
            else:
                complement += '1'
        return int(complement, 2)


sol = Solution()
print(sol.findComplement(5))
