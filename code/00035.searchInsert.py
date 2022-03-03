# -- coding: utf-8 --

# easy

class Solution:
    def searchInsert(self, nums, target):
        left, right = 0, len(nums)
        while (left < right):
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
            else:
                return mid
        return left