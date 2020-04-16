from typing import List


class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        left_shift = 0
        for single_shift in shift:
            if single_shift[0] == 0:
                left_shift += single_shift[1]
            else:
                left_shift -= single_shift[1]

        s = list(s)
        if left_shift > 0:
            for _ in range(left_shift):
                item = s.pop(0)
                s.append(item)
        elif left_shift < 0:
            for _ in range(abs(left_shift)):
                item = s.pop()
                s.insert(0, item)

        return ''.join(s)


sol = Solution()
s = "wpdhhcj"
shift = [[0, 7], [1, 7], [1, 0], [1, 3], [0, 3], [0, 6], [1, 2]]
print(sol.stringShift(s, shift))
