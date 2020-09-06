from typing import List
from collections import Counter


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0
        
        count = Counter(nums)
        pairs = set([])

        for num in count.keys():
            if k == 0:
                if count[num] > 1:
                    pairs.add((num, num))
            else:
                anotherNum = num + k
                if anotherNum in count:
                    pairs.add((num, anotherNum))

        return len(pairs)



sol = Solution()
nums = [3, 1, 4, 1, 5]
k = 2
print(sol.findPairs(nums, k))
