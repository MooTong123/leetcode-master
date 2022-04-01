# -- coding: utf-8 --
'''
哈希表第7节：四数相加II 454
medium
'''

class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """

        countAB = dict()
        for n1 in nums1:
            for n2 in nums2:
                if n1 + n2 in countAB:
                    countAB[n1 + n2] += 1
                else:
                    countAB[n1 + n2] = 1

        count = 0
        for n3 in nums3:
            for n4 in nums4:
                key = - n3 - n4
                if key in countAB:
                    count += countAB[key]

        return count