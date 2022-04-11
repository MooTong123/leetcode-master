# -- coding: utf-8 --
'''
offer58: 左旋转字符串 easy
切片

'''

class Solution(object):
    def reverseLeftWords(self, s, n):
        """
        :type s: str
        :type n: int
        :rtype: str
        """

        return s[n:] + s[:n]