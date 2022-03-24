# -- coding: utf-8 --
'''
350. 两个数组的交集 II
哈希表
easy
'''

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = Counter(nums1) & Counter(nums2)
        return list(count.elements())