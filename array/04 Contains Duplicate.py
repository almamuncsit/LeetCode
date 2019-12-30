# Contains Duplicate


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        old_len = len(nums)
        new_len = len( list(set(nums)) )
        
        return old_len != new_len