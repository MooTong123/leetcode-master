# -- coding: utf-8 --

'''
字符串第二节：反转字符串 541
easy
'''

class Solution(object):

    def reverseString(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s

    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """

        res = list(s)
        for i in range(0, len(s), 2 * k):
            res[i: i + k] = self.reverseString(res[i: i + k])
        return ''.join(res)

