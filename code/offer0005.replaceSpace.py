# -- coding: utf-8 --
'''
字符串第三节：剑指offer0005.替换空格
easy

'''

class Solution(object):
    def replaceSpace(self, s):
        """
        :type s: str
        :rtype: str
        """

        count = s.count(' ')
        res = list(s)
        res.extend(' ' * count * 2)

        left, right = len(s) - 1, len(res) - 1

        while left >= 0:
            if res[left] == ' ':
                res[right-2: right+1] = '%20'
                right -= 3
            else:
                res[right] = res[left]
                right -= 1
            left -= 1
        return ''.join(res)