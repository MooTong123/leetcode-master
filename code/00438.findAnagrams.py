# -- coding: utf-8 --

'''
438. 找到字符串中所有字母异位词
medium
哈希表+滑动窗口

'''

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        m = len(p)
        n = len(s)
        results = []

        if m > n:
            return []

        count_s = [0] * 26
        count_p = [0] * 26

        for i in range(m):
            count_s[ord(s[i]) - ord('a')] += 1
            count_p[ord(p[i]) - ord('a')] += 1

        if count_p == count_s:
            results.append(0)

        for i in range(m, n):
            count_s[ord(s[i - m]) - ord('a')] -= 1
            count_s[ord(s[i]) - ord('a')] += 1

            if count_s == count_p:
                results.append(i - m + 1)
        return results