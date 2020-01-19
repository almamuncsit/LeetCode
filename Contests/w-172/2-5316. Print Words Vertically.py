class Solution:
    def printVertically(self, s):
    	str_list = s.split(' ')
    	max_iter = max(map(len, str_list))
    	vertical_list = []
    	for x in range(max_iter):
    		new_item = []
    		for item in str_list:
    			if x < len(item):
    				new_item.append(item[x])
    			else:
    				new_item.append(' ')
    		vertical_list.append( ( ''.join(new_item)).rstrip() )

    	return vertical_list


sol = Solution()
s = "TO BE OR NOT TO BE"
print( sol.printVertically(s) )