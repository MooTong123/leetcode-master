# -- coding: utf-8 --
'''
数组5：滑动窗口
hard

步骤一
不断增加j使滑动窗口增大，直到窗口包含了T的所有元素

步骤二
不断增加i使滑动窗口缩小，因为是要求最小字串，所以将不必要的元素排除在外，使长度减小，直到碰到一个必须包含的元素，这个时候不能再扔了，再扔就不满足条件了，记录此时滑动窗口的长度，并保存最小值

步骤三
让i再增加一个位置，这个时候滑动窗口肯定不满足条件了，那么继续从步骤一开始执行，寻找新的满足条件的滑动窗口，如此反复，直到j超出了字符串S范围。


'''


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.defaultdict(int)
        need_count = 0
        res = (0, float("inf"))
        left = 0

        for c in t:
            need[c] += 1
            need_count += 1

        # 步骤1：滑动右指针，直到发现所有元素集齐了
        for right in range(len(s)):
            if need[s[right]] > 0:
                need_count -= 1

            need[s[right]] -= 1

            # 发现所需元素集齐了
            if need_count == 0:

                # 步骤二：左指针向左移动，直到再移动就集不齐元素了
                while True:
                    if need[s[left]] == 0:
                        break
                    else:
                        need[s[left]] += 1
                        left += 1

                # 记录结果
                if right - left < res[1] - res[0]:
                    res = (left, right)

                # 步骤三：左指针再向右移动一个，元素集不齐，进入大循环，继续移动右指针
                need[s[left]] += 1
                need_count += 1
                left += 1

        if res[1] > len(s):
            return ''
        else:
            return s[res[0]:res[1] + 1]
