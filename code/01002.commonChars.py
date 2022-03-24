# -- coding: utf-8 --
'''
查找常用字符
哈希表
easy
'''

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:

        # 记录第一个词的count
        hash_minimum = [0] * 26
        for i in words[0]:
            hash_minimum[ord(i) - ord('a')] += 1

        # 循环剩下的str
        for i in range(1, len(words)):
            hash_other_str = [0] * 26
            for j in words[i]:
                hash_other_str[ord(j) - ord('a')] += 1

            # 更新hash_minimum最小值
            for k in range(26):
                hash_minimum[k] = min(hash_minimum[k], hash_other_str[k])

        results = []
        for i in range(26):
            while hash_minimum[i] != 0:
                results.append(chr(i + ord('a')))
                hash_minimum[i] -= 1

        return results
