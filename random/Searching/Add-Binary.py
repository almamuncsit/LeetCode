class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_rev = a[::-1]
        b_rev = b[::-1]
        output = ''
        carry = 0
        
        for i in range( max(len(a_rev), len(b_rev)) ):
            first_number = 0 if (i >= len(a_rev)) else int(a_rev[i])
            second_number = 0 if (i >= len(b_rev)) else int(b_rev[i])
            bit_sum = first_number + second_number + carry
            if bit_sum == 3:
                output = '1' + output
                carry = 1
            elif bit_sum == 2:
                output = '0' + output
                carry = 1
            elif bit_sum == 1:
                output = '1' + output
                carry = 0
            else:
                output = '0' + output
                carry = 0
        
        if carry == 1:
            output = '1' + output
        
        return output



sol = Solution()
a = "11"
b = "1"
print(sol.addBinary(a, b))
