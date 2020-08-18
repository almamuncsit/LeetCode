from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for item in strs:
            sorted_item = ''.join(sorted(item))
            anagrams[sorted_item].append(item)

        return list(anagrams.values())


sol = Solution()
str_arr = ["cab", "tin", "pew", "duh", "may", "ill", "buy", "bar", "max", "doc"]
# str_arr = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(sol.groupAnagrams(str_arr))
