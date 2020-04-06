class Solution:
    def numSteps(self, s: str) -> int:
        number = int(s, 2)
        steps = 0

        while number != 1:
            if number % 2 == 1:
                number += 1
            else:
                number = number >> 1

            steps += 1

        return steps


sol = Solution()
st = "1111011110000011100000110001011011110010111001010111110001"
print(sol.numSteps(st))
