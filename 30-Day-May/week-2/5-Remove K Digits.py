class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for c in num:
            while len(stack) > 0 and stack[-1] > c and k > 0:
                stack.pop()
                k -= 1
            stack.append(c)
        if k > 0:
            stack = stack[:-k]

        return ''.join(stack).lstrip('0') or '0'


sol = Solution()
print(sol.removeKdigits("9", 1))
