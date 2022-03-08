
'''
滑动窗口法
1. 确定左边界和右边界，左右边界怎么滑动？
2. 分情况讨论即可

'''

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        if n <= 2:
            return n

        left = -1
        right = -1

        res = 0
        max_res = 0

        for i in range(n):
            if i == 0:
                left = i
                res += 1
                continue
            elif fruits[i] == fruits[left] and right == -1:
                res += 1
                continue
            elif fruits[i] != fruits[left] and right == -1:
                right = i
                res += 1
                continue

            if not (fruits[i] == fruits[left] or fruits[i] == fruits[right]):
                max_res = max(max_res, res)
                left = right
                right = i
                res = right - left + 1
            elif fruits[i] == fruits[left]:
                left = right
                right = i
                res += 1
            elif fruits[i] == fruits[right]:
                res += 1

        max_res = max(max_res, res)

        return max_res