class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        soldier_dic = { idx:k.count(1) for idx, k in enumerate(mat) }
        sorted_soldier = {k: v for k, v in sorted(soldier_dic.items(), key=lambda x: x[1])}
        return list(sorted_soldier)[:k]

mat = [[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]] 
k = 3        
sol = Solution()
sol.kWeakestRows(mat, k)