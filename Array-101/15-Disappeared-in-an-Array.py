from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        disappeard = []
        nums_dic = {}
        
        for num in nums:
            nums_dic[num] = 1
        
        for i in range(1, len(nums)+1):
            if i not in nums_dic:
                disappeard.append(i)
        
        return disappeard



sol = Solution()
nums = [4, 3, 2, 7, 8, 2, 3, 1]
disappeared = sol.findDisappearedNumbers(nums)
print(disappeared)