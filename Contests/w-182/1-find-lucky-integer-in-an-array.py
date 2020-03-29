from collections import Counter

class Solution:
    def findLucky(self, arr: List[int]) -> int:
    	lucky = -1
    	freequecy_count = Counter(arr)
    	for key, value in freequecy_count.items():
    		if key == value and key > lucky:
    			lucky = key

    	return lucky


sol = Solution()
arr = [7,7,7,7,7,7,7]
print( sol.findLucky(arr) )
        