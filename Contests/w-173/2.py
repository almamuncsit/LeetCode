class Solution:
    def filterRestaurants(self, restaurants, veganFriendly, maxPrice, maxDistance):
    	solArr = []
    	for r in restaurants:
    		added = False
    		if veganFriendly == 0:
    			if r[3] <= maxPrice and r[4] <= maxDistance:
    				solArr.append(r)
    		else:
    			if r[2] == veganFriendly and r[3] <= maxPrice and r[4] <= maxDistance:
    				solArr.append(r)

    	solArr = sorted(solArr,key=lambda x: x[1], reverse=True)

    	for x in range(len(solArr) - 2):
    		if solArr[x][1] == solArr[x+1][1] and solArr[x][0] < solArr[x+1][0]:
    			solArr[x], solArr[x+1] = solArr[x+1], solArr[x]

    	return [ item[0] for item in solArr]
        


restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]]
veganFriendly = 0
maxPrice = 50 
maxDistance = 10

solution = Solution()
print(solution.filterRestaurants(restaurants, veganFriendly, maxPrice, maxDistance))