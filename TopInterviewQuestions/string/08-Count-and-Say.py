class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        
        string = '11'

        for _ in range(2, n):
            output = ''
            count = 0
            last_seen = ''
            
            for c in string:
                if not last_seen or last_seen == c:
                    count += 1
                    last_seen = c
                else:
                    output += str(count) + last_seen
                    count = 1
                    last_seen = c
            
            output += str(count) + last_seen
            string = output
        
        return string
 


sol = Solution()
n = 3
print(sol.countAndSay(n))
