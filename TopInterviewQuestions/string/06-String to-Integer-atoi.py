class Solution:
    def myAtoi(self, str: str) -> int:
        s = str.strip()
        output = []

        if not s:
            return 0

        if s[0] in ['-', '+'] or s[0].isnumeric():
            output.append(s[0])
        else:
            return 0
        
        for x in range(1, len(s)):
            if s[x].isnumeric():
                output.append(s[x])
            else:
                break 
        
        if len(output) == 1 and output[0] in ['-', '+']:
            return 0
        
        output_number = int(''.join(output))
        if output_number > (pow(2, 31)-1):
            return pow(2, 31) - 1
        elif output_number < -(pow(2, 31)):
            return -(pow(2, 31))
        else:
            return output_number


sol = Solution()
s = ""
print(sol.myAtoi(s))
