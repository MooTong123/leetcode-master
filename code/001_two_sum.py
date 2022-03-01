# -- coding: utf-8 --


class Solution:
    def twoSum(self, nums, target):
        '''
        :param nums: List[int]
        :param target: : int
        :return:List[int]
        '''

        table = {}
        for i, value in enumerate(nums):
            if target - value not in table:
                table[value] = i
            else:
                return [i, table[target - value]]


