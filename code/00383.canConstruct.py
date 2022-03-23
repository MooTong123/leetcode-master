# -- coding: utf-8 --
'''
383. 赎金信
easy
哈希表
'''

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import defaultdict

        str_dict = defaultdict(int)
        for x in magazine:
            str_dict[x] += 1

        for x in ransomNote:
            str_dict[x] -= 1

        for value in str_dict.values():
            if value < 0:
                return False

        return True