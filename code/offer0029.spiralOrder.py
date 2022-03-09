# -- coding: utf-8 --

'''
螺旋数组 easy

'''

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        if not matrix:
            return []

        left, right, up, bottom = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        res = []

        while True:

            # 从左往右
            for x in range(left, right + 1, 1):
                res.append(matrix[up][x])
            up += 1
            if up > bottom:
                break

            # 从上到下
            for x in range(up, bottom + 1, 1):
                res.append(matrix[x][right])
            right -= 1
            if right < left:
                break

            # 从右往左
            for x in range(right, left - 1, -1):
                res.append(matrix[bottom][x])
            bottom -= 1
            if bottom < up:
                break

            # 从下往上
            for x in range(bottom, up - 1, -1):
                res.append(matrix[x][left])
            left += 1
            if left > right:
                break

        return res

