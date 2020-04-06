class Solution(object):
    def longestDiverseString(self, a, b, c):
        my_array = [[a, 'a'], [b, 'b'], [c, 'c']]
        answer = []
        for _ in range(a+b+c):
            my_array.sort(reverse=True)
            for i in range(3):
                if my_array[i][0] == 0:
                    continue
                if len(answer) < 2 or not(answer[-1] == answer[-2] == my_array[i][1] ):
                    answer.append(my_array[i][1])
                    my_array[i][0] -= 1
                    break

        return "".join(answer)


sol = Solution()

print(sol.longestDiverseString(7, 1, 0))
