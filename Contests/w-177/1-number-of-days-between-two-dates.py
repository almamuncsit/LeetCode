import datetime


class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        date1 = datetime.datetime.strptime(date1, '%Y-%m-%d').date()
        date2 = datetime.datetime.strptime(date2, '%Y-%m-%d').date()
        return abs((date2 - date1).days)


date1 = "2020-01-15"
date2 = "2019-10-30"
sol = Solution()
print(sol.daysBetweenDates(date1, date2))
