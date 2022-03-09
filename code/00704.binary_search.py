# -- coding: utf-8 --

'''
数组2：二分法
easy

'''

class Solution:

    def search(self, nums, target) :
        '''
        二分法
        :param nums: List[int]
        :param target: int
        :return: int
        '''

        left, right = 0, len(nums)
        while (left < right):
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                # 不是 mid - 1
                right = mid
            else:
                return mid

        return -1



