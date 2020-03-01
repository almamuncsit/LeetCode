class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
    	counts = [0] * len(nums)
    	for x in range(len(nums)):
    		for n in nums:
    			if n < nums[x]:
    				counts[x] += 1

    	return counts

sol = Solution()
nums = [7,7,7,7]
print(sol.smallerNumbersThanCurrent(nums))