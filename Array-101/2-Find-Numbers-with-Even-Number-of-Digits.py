from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        event_digit = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                event_digit += 1
        return event_digit
