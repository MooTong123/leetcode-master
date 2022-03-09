# -- coding: utf-8 --
'''
数组6：螺旋矩阵
medium

定义好区间，左闭右开

'''

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # 建立matrix
        matrix = [[0] * n for _ in range(n)]

        left, right, up, bottom = 0, n - 1, 0, n - 1
        number = 1

        while left < right and up < bottom:

            # 从左往右
            for x in range(left, right, 1):
                matrix[up][x] = number
                number += 1

            # 从上到下
            for x in range(up, bottom, 1):
                matrix[x][right] = number
                number += 1

            # 从右到左
            for x in range(right, left, -1):
                matrix[bottom][x] = number
                number += 1

            # 从下到上
            for x in range(bottom, up, -1):
                matrix[x][left] = number
                number += 1

            left += 1
            up += 1
            right -= 1
            bottom -= 1

        if n % 2 == 1:
            matrix[n // 2][n // 2] = number

        return matrix