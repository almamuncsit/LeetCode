from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note_count = Counter(ransomNote)
        magazine_count = Counter(magazine)
        for note in note_count.keys():
            if note not in magazine_count or note_count[note] > magazine_count[note]:
                return False
        return True


sol = Solution()
print(sol.canConstruct('aac', 'aab'))
