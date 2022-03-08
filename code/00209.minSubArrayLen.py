# -- coding: utf-8 --

'''
滑动窗口法
1. 窗口就是 满足其和 ≥ s 的长度最小的 连续 子数组。
2. 窗口的起始位置如何移动：如果当前窗口的值大于s了，窗口就要向前移动了（也就是该缩小了）。
3. 窗口的结束位置如何移动：窗口的结束位置就是遍历数组的指针，窗口的起始位置设置为数组的起始位置就可以了。
'''


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float("inf")
        sum = 0
        index = 0

        for i in range(len(nums)):
            sum += nums[i]
            while sum >= target:
                res = min(res, i - index + 1)
                sum -= nums[index]
                index += 1

        if res == float("inf"):
            return 0
        else:
            return res