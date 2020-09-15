class Solution:
    def reverseVowels(self, s: str) -> str:
        s_list = list(s)
        vowels = set({'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'})
        left = 0
        right = len(s_list)-1
        while right > left:
            if s_list[left] in vowels and s_list[right] in vowels:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1
            else:
                if s_list[left] not in vowels:
                    left += 1
                if s_list[right] not in vowels:
                    right -= 1

        return ''.join(s_list)


sol = Solution()
print(sol.reverseVowels("leetcode"))
