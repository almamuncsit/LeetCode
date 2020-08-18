from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        sorted_words = sorted(words, key=len)
        sub_strs = set()
        for i in range(len(sorted_words)):
            for j in range(i + 1, len(sorted_words)):
                if sorted_words[i] in sorted_words[j]:
                    sub_strs.add(sorted_words[i])
                    continue
        return list(sub_strs)


words = ["leetcoder", "leetcode", "od", "hamlet", "am"]
sol = Solution()
print(sol.stringMatching(words))
