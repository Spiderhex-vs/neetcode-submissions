class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for i, num in enumerate(nums):
            needed = target - num
            if needed in seen.keys():
                solution = [seen[needed], i]
                solution.sort()
                return solution
            seen[num] = i