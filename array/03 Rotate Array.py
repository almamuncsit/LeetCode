# Rotate Array

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        old_len = len(nums)
        for _ in range(0, k):
            nums.append(0)

        length = len(nums)

        for i in range(length, 0, -1):
            nums[i-1] = nums[i-(k+1)]
        
        for _ in range(0, k):
            nums.pop()
            
        