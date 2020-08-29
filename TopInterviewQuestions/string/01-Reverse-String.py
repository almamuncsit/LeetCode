from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        i = 0
        j = len(s)-1
        while j > i:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

        return s

if __name__ == "__main__":
    sol = Solution()
    input_str = ["H", "a", "n", "n", "a", "h"]
    print(sol.reverseString(input_str))
