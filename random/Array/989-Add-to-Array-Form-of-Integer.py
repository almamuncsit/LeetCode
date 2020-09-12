from typing import List


# class Solution:
# 	def addToArrayForm(self, A: List[int], K: int) -> List[int]:
# 		A = map(str, A)
# 		a_num = int(''.join(A))
# 		total = a_num + K
# 		return list(str(total))

# Solution using math technic
class Solution:
	def addToArrayForm(self, A: List[int], K: int) -> List[int]:
		A[-1] += K
		for i in range(len(A)-1, -1, -1):
			carry, A[i] = divmod(A[i], 10)
			print(carry, i, A[i])
			if i:
				A[i-1] += carry
		
		if carry:
			A.insert(0, carry)
		
		return A


sol = Solution()
A = [2, 1, 5]
K = 806
print(sol.addToArrayForm(A, K))        
