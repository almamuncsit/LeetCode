from typing import List


class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        sum_arr = []
        sum_of_evens = 0
        for item in A:
            if item % 2 == 0:
                sum_of_evens += item

        for query in queries:
            if A[query[1]] % 2 == 0:
                sum_of_evens -= A[query[1]]
            
            A[query[1]] += query[0]
            if A[query[1]] % 2 == 0:
                sum_of_evens += A[query[1]]
            
            sum_arr.append(sum_of_evens)
        
        return sum_arr


sol = Solution()
A = [1, 2, 3, 4]
queries = [[1, 0], [-3, 1], [-4, 0], [2, 3]]
print(sol.sumEvenAfterQueries(A, queries))
