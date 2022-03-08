# -- coding: utf-8 --

'''
双指针法
easy

思路：
1. 非递减顺序，所以平方的最大值永远在最左侧或者最右侧！

'''

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right, write = 0, len(nums) - 1, len(nums) - 1

        results = [0] * (write + 1)

        while (left <= right):
            if nums[left] * nums[left] <= nums[right] * nums[right]:
                results[write] = nums[right] * nums[right]
                right -= 1
            else:
                results[write] = nums[left] * nums[left]
                left += 1

            write -= 1

        return results