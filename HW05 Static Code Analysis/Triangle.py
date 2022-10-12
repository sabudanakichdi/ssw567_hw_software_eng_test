# -*- coding: utf-8 -*-
"""
Created on Oct 12, 2022
The primary goal of this file is to demonstrate a simple python program to classify triangles
@author: Prateek Chauhan
"""

def classify_triangle(side_1,side_2,side_3):
    """Classifies Triangle"""
    if not(isinstance(side_1,int) and isinstance(side_2,int) and isinstance(side_3,int)):
        return 'InvalidInput'

    if side_1 > 200 or side_2 > 200 or side_3 > 200:
        return 'InvalidInput'

    if side_1 <= 0 or side_2 <= 0 or side_3 <= 0:
        return 'InvalidInput'

    if (side_1 > (side_2 + side_3)) or (side_2 > (side_1 + side_3)) or (side_3 > (side_1 + side_2)):
        return 'NotATriangle'

    if side_1 == side_2 and side_2 == side_1 and side_3==side_1:
        return 'Equilateral'
    if ((((side_1 ** 2) + (side_2 ** 2)) == (side_3 ** 2))
          or (((side_2 ** 2) + (side_3 ** 2)) == (side_1 ** 2))
          or (((side_1 ** 2) + (side_3 ** 2)) == (side_2 ** 2))):
        return 'Right'
    if (side_1 != side_2) and  (side_2 != side_3) and (side_1 != side_3):
        return 'Scalene'
    return 'Isoceles'
