class SolutionOne:
    def hammingDistance(self, x: int, y: int) -> int:
        x_bit = list(bin(x)[2:])
        y_bit = list(bin(y)[2:])

        if len(x_bit) > len(y_bit):
            max_bit, min_bit = x_bit, y_bit
        else:
            min_bit, max_bit = x_bit, y_bit

        for i in range(len(min_bit), len(max_bit)):
            min_bit.insert(0, '0')

        ans = 0
        for i in range(len(max_bit)):
            if min_bit[i] != max_bit[i]:
                ans += 1

        return ans


# Another Best Solution
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        bit_diff = bin(x ^ y)
        return bit_diff.count('1')


sol = Solution()
print(sol.hammingDistance(1, 4))
