# -- coding: utf-8 --


class Solution:
    '''
    easy
    二分法
    '''


    def mySqrt(self, x: int) -> int:
        left, right, result = 0, x, -1

        if x == 0:
            return 0
        if x == 1:
            return 1

        while (left < right):
            mid = (left + right) // 2
            if mid * mid < x:
                result = mid
                left = mid + 1
            elif mid * mid > x:
                right = mid
            else:
                return mid

        return result
