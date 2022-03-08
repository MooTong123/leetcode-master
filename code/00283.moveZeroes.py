# -- coding: utf-8 --
'''
easy
双指针法

思路：
1. 左指针代表 已处理好的序列的最右侧
2. 右指针代表 未处理的序列的最左侧
3. 左右指针中间的是 0

'''

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        slow, fast = 0, 0
        while fast < len(nums):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
            fast += 1

        return nums