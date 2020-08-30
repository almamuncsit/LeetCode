from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        prefix = strs[0]
        temp_prefix = ""

        for x in range(1, len(strs)):
            temp_prefix = ""
            min_len = min(len(prefix), len(strs[x]))
            for i in range(min_len):
                if prefix[i] == strs[x][i]:
                    temp_prefix += prefix[i]
                else:
                    break
            
            prefix = temp_prefix
            if not prefix:
                return ""
        
        return prefix


sol = Solution()
string_list = ["dog", "racecar", "car"]
print(sol.longestCommonPrefix(string_list))
