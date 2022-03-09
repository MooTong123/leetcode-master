# -- coding: utf-8 --

'''
数组6：螺旋矩阵
medium

思路：更新所有边界
'''

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        m = len(matrix)
        n = len(matrix[0])

        left, right, up, bottom = 0, n - 1, 0, m - 1
        res = []

        # 更新所有边界 ！！！！

        while True:

            # 从左到右
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

            # 从右到左
            for x in range(right, left - 1, -1):
                res.append(matrix[bottom][x])
            bottom -= 1
            if bottom < up:
                break

            # 从下到上
            for x in range(bottom, up - 1, -1):
                res.append(matrix[x][left])
            left += 1
            if left > right:
                break

        return res