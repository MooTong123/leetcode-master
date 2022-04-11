# -- coding: utf-8 --

'''
151.颠倒字符串中的单词
字符串第四节
medium

尝试用O(1),直接操作字符串来做
'''

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(reversed(s.split()))