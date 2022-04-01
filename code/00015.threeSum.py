# -- coding: utf-8 --

'''
15. 三数之和
哈希表第9节：
双指针法
medium

'''
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 哈希表可以做，但是判断重复太繁琐，所以用双指针法
        # 双指针适合返回数值，因为要用sort，所以返回下标的不能用双指针法
        results = []
        nums.sort()
        n = len(nums)
        for i in range(n):
            left = i + 1
            right = n - 1
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while left < right:

                total = nums[i] + nums[left] + nums[right]
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    results.append([nums[i], nums[left], nums[right]])
                    while left != right and nums[left] == nums[left + 1]:
                        left += 1
                    while left != right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        return results
