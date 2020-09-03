class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
            else:
                if not stack:
                    return False
                l = stack.pop()
                if (c == ")" and l != '(') or (c == "}" and l != '{') or (c == "]" and l != '['):
                    return False
        
        return len(stack) == 0


sol = Solution()
s = "{[]}"
print(sol.isValid(s))
