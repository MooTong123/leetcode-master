# -- coding: utf-8 --

# medium

# 1 3 5 6 8

class Solution:
    def searchRange(self, nums, target) :
        def binarySearch(nums, target):
            left, right = 0, len(nums)
            while(left < right):
                mid = (left + right) // 2
                if mid < target:
                    left = mid + 1
                elif mid > target:
                    right = target
                else:
                    return mid
            return -1

        index = binarySearch(nums,target)

        if index == -1:
            return [-1,-1]

        

