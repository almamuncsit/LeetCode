# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        if isBadVersion(1):
            return 1
        if not isBadVersion(n):
            return n
        left, right = 1, n
        while left <= right:
            mid = left + (right - left) // 2
            if isBadVersion(mid) and not isBadVersion(mid - 1):
                return mid
            elif not isBadVersion(mid) and isBadVersion(mid + 1):
                return mid + 1
            elif isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1
