class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        seen = set(nums)
        seen = sorted(seen)

        highest_len = 0
        current_len = 1
        prev = seen[0]
        for num in seen:
            if num - prev == 1:
                current_len += 1
                prev = num
            elif num == prev:
                continue
            else:
                highest_len = max(highest_len, current_len)
                current_len = 1
                prev = num

        highest_len = max(highest_len, current_len)
        return highest_len
