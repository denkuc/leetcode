from typing import List


class Solution:
    def removeElement(self, nums: List[int]) -> int:
        n = len(nums) - 1
        while n > 0:
            if nums[n-1] == nums[n]:
                nums.pop(n)
            n -= 1

        return len(nums)
