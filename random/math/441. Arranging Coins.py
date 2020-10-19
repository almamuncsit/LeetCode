class Solution:
    def arrangeCoins(self, n: int) -> int:
        full_staircase = 0
        stage = 1
        while n >= stage:
            full_staircase += 1
            n -= stage
            stage += 1

        return full_staircase
