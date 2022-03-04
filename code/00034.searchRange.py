# -- coding: utf-8 --


class Solution:
    '''
       medium
       二分法
       '''

    def searchRange(self, nums, target):
        def binarySearch(nums, target):
            left, right = 0, len(nums)
            while (left < right):
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid
                else:
                    return mid
            return -1

        index = binarySearch(nums, target)

        if index == -1:
            return [-1, -1]

        left, right = index, index

        while left - 1 >= 0:
            if nums[left - 1] == nums[left]:
                left = left - 1
            else:
                break

        while right + 1 < len(nums):
            if nums[right + 1] == nums[right]:
                right = right + 1
            else:
                break

        return [left, right]

