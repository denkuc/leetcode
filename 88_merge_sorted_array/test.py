import unittest
from solution import Solution


class SolutionTest(unittest.TestCase):
    def test_1(self):
        nums1 = [1, 2, 3, 0, 0, 0]
        m = 3
        nums2 = [2, 5, 6]
        n = 3
        Solution().merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1, 2, 2, 3, 5, 6])

    def test_2(self):
        nums1 = [1]
        m = 1
        nums2 = []
        n = 0
        Solution().merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1])

    def test_3(self):
        nums1 = [0]
        m = 0
        nums2 = [1]
        n = 1
        Solution().merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1])

    def test_4(self):
        nums1 = [1,0]
        m = 1
        nums2 = [2]
        n = 1
        Solution().merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1,2])

    def test_5(self):
        nums1 = [4,0,0,0,0,0]
        m = 1
        nums2 = [1,2,3,5,6]
        n = 5
        Solution().merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1,2,3,4,5,6])
