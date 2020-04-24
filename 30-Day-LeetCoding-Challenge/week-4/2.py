class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        # shift = m
        # m += 1
        # while m != n:
        #     shift &= m
        #     m += 1
        # return shift

        shift = 0
        while m != n:
            m >>= 1
            n >>= 1
            print(m, n)
            shift += 1
        return m << shift


sol = Solution()
print(sol.rangeBitwiseAnd(5, 7))
