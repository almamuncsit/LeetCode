class Solution:
    def reverse(self, x: int) -> int:
        x_str = list(reversed(list(str(x))))
        if x_str[-1] == '-':
            x_str.insert(0, x_str.pop())

        output = int(''.join(x_str))

        if output > 0 and output > ((pow(2, 31))-1):
            return 0
        elif output < 0 and output < -pow(2, 31):
            return 0

        return output
