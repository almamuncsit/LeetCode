class Solution:
    def hammingWeight(self, n: int) -> int:
        number_of_one = 0
        binary = str(bin(n)[2:])

        for digit in binary:
            if digit == '1':
                number_of_one += 1

        return number_of_one
