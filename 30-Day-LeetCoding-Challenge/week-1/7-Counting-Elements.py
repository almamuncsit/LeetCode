from typing import List


class Solution:
    def countElements(self, arr: List[int]) -> int:
        arr.sort()
        last_count = 1
        last_num = arr[0]
        total_count = 0
        for i in range(1, len(arr)):
            if last_num == arr[i]:
                last_count += 1
            elif arr[i] == last_num + 1:
                total_count += last_count
                last_num = arr[i]
                last_count = 1
            else:
                last_num = arr[i]
                last_count = 1

        return total_count


sol = Solution()
ar = [1, 1, 2, 2]
print(sol.countElements(ar))
