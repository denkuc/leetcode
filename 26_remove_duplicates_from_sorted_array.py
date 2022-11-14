from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]):
        index = 0
        for jndex, num in enumerate(nums):
            if nums[jndex] != nums[index]:
                nums[index] = nums[jndex]
                index += 1
        return index + 1


assert Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]) == [0,1,2,3,4]