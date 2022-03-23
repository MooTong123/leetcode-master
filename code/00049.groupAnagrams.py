# -- coding: utf-8 --
'''
49. 字母异位词分组
medium
哈希表
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        str_dict = defaultdict(list)

        for x in strs:
            key_x = ''.join(sorted(x))
            str_dict[key_x].append(x)

        # results = []
        # for value in str_dict.values():
        #     results.append(value)
        # return results

        return list(str_dict.values())