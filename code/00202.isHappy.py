# -- coding: utf-8 --
'''
202. 快乐数
哈希第5节
easy
'''


class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_num(num):
            sum = 0
            while num != 0:
                sum += (num % 10) ** 2
                num = num // 10

            return sum

        happy_set = set()

        while True:
            n = sum_num(n)
            if n == 1:
                return True

            if n in happy_set:
                return False
            else:
                happy_set.add(n)