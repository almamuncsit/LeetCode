class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        for c in J:
            count += S.count(c)
        return count


sol = Solution()
J = "z"
S = "ZZ"
print(sol.numJewelsInStones(J, S))
