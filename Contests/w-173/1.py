class Solution:
	
	def isPalindrom(self, str):
		l = 0
		h = len(str)-1
		while h > l:
			if str[l] is not str[h]:
				return 0;
			l += 1
			h -= 1
		return 1

    def removePalindromeSub(self, s: str) -> int:
    	if str[0] == '':
    		return 0
    	if self.isPalindrom(str):
    		return 1
    	return 2


s = "baab"
solution = Solution()
print(solution.isPalindrom(s))
solution.removePalindromeSub(s)
        