# -- coding: utf-8 --

# easy

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 0, num

        if num == 1:
            return True

        while (left < right):
            mid = (left + right) // 2
            if mid * mid < num:
                left = mid + 1
            elif mid * mid > num:
                right = mid
            else:
                return True

        return False