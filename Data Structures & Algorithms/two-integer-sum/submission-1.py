class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for i, num in enumerate(nums):
            needed = target - num
            if needed in seen.keys():
                return [seen[needed], i]
            seen[num] = i