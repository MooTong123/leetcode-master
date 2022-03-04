# -- coding: utf-8 --

'''
easy
双指针法
'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if not nums:
            return 0

        slow, fast = 1, 1
        while fast < len(nums):
            if nums[fast - 1] != nums[fast]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1

        return slow