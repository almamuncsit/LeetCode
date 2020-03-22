class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
    	target = []
    	for i in range(len(index)):
    		target.insert(index[i], nums[i])

    	return target

nums = [0,1,2,3,4] 
index = [0,1,2,2,1]

sol = Solution()
print(sol.createTargetArray(nums, index))