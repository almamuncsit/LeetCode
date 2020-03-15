class Solution:
    def luckyNumbers (self, matrix):
    	m = len(matrix)
    	n = len(matrix[0])
    	lucky = []
    	for i in range(m):
    		for j in range(n):
    			num = matrix[i][j]
    			if self.isLucky(matrix, num, i, j):
    				lucky.append(num)
    	return lucky

    def isLucky(self, matrix, num, row, col):
    	for x in range(len(matrix[0])):
    		if num > matrix[row][x]:
    			return False
    	for x in range(len(matrix)):
    		if num < matrix[x][col]:
    			return False
    	return True
		

mat = [	[3, 7, 8], 
		[9, 11, 13], 
		[15, 16, 17] ]
matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
sol = Solution()
print(sol.luckyNumbers(matrix))
