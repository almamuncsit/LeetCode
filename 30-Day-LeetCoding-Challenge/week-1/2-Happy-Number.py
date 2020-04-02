class Solution:

    def isHappy(self, n: int):
        look_up = {}
        while True:
            if n == 1:
                return True
            elif n in look_up:
                return False
            look_up[n] = 1
            n = sum(map(lambda x: (int(x) ** 2), str(n)))


sol = Solution()
print(sol.isHappy(19))
