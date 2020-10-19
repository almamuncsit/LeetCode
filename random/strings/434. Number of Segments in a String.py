class Solution:
    def countSegments(self, s: str) -> int:
        s = s.strip()
        num = 0
        for item in s.split(' '):
            if item and item is not " ":
                num += 1

        return num
