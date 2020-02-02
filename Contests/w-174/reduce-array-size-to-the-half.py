class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        arr_len = len(arr)
        arr_set = set(arr)
        num_count = {}
        for item in arr:
            if num_count[item]:
                num_count[item] += 1
            else:
                num_count[item] = 1

        sorted_nums = {k: v for k, v in sorted(num_count.items(), key=lambda x: x[1], reverse=True)}
        set_count = 0
        removed_size = 0 
        for num, count in sorted_nums.items():
            set_count += 1
            removed_size += count
            if removed_size >= (arr_len / 2):
                return set_count



arr = [1,2,3,4,5,6,7,8,9,10]
sol = Solution()
print(sol.minSetSize(arr))