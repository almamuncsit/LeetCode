class Solution:
    def rankTeams(self, votes: List[str]) -> str:
    	ranks = {}
    	if len(votes) == 1:
    		return votes[0]

    	for vote in votes:
    		for x in range(len(vote)):
    			if vote[x] not in ranks:
    				ranks[vote[x]] = [0]*len(vote)

    			ranks[vote[x]][x] +=1
    	for key in ranks.keys():
    		ranks[key].append( ord('z') - ord(key) )
    	
    	new_ranks = list(ranks.values())
    	new_ranks.sort(reverse=True)

    	items = [chr(ord('z') - x[-1]) for x in new_ranks]
    	return ''.join(items)


sol = Solution()
votes = ["M","M","M","M"]
print(sol.rankTeams(votes));