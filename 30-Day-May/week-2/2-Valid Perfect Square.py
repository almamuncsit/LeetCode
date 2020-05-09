class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low, high = 1, num
        while low <= high:
            mid = (high + low) // 2
            square = mid * mid
            print(low, high, mid)
            if square == num:
                return True
            elif square < num:
                low = mid + 1
            else:
                high = mid - 1
        return False


sol = Solution()
print(sol.isPerfectSquare(16))
