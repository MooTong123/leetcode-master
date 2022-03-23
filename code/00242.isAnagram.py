# -- coding: utf-8 --
'''
242. 有效的字母异位词
easy
哈希表
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict

        str_dict = defaultdict(int)

        for i in s:
            str_dict[i] += 1

        for i in t:
            str_dict[i] -= 1

        for value in str_dict.values():
            if value != 0:
                return False

        return True



