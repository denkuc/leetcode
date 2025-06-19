from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for index, num in enumerate(nums):
            if num >= target:
                return index
        return len(nums)

assert Solution().searchInsert([1,3,5,6], 5) == 2
assert Solution().searchInsert([1,3,5,6], 2) == 1
assert Solution().searchInsert([1,3,5,6], 7) == 4
assert Solution().searchInsert([1,3,5,6], 0) == 0