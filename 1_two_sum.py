from typing import List


class Solution:
    def twoSumBrute(self, nums: List[int], target: int) -> List[int]:
            indexes = []
            for index_i, num_i in enumerate(nums):
                for index_j, num_j in enumerate(nums[index_i+1:]):
                    if num_i+num_j == target:
                        indexes = [index_i, index_j+index_i+1]

            return indexes

    def twoSumTwoPassHash(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for index_i, num_i in enumerate(nums):
            if nums_dict.get(num_i) is not None:
                nums_dict[num_i] = [nums_dict[num_i], index_i]
            else:
                nums_dict[num_i] = index_i

        for num_i, index_i in nums_dict.items():
            complement = target - num_i
            index_j = nums_dict.get(complement)
            if isinstance(index_j, list):
                return index_j
            if index_j is not None and index_i != index_j:
                return [index_i, index_j]

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for index_i, num_i in enumerate(nums):
            complement = target - num_i
            index_j = nums_dict.get(complement)
            if index_j is not None:
                return [index_i, index_j]

            nums_dict[num_i] = index_i


print(Solution().twoSum([3, 3], 6))
