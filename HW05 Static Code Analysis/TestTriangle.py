# -*- coding: utf-8 -*-
"""
Updated Oct 12, 2022
The primary goal of this file is to demonstrate a simple unittest implementation
@author: Prateek Chauhan
"""

import unittest

from Triangle import classify_triangle

class TestTriangles(unittest.TestCase):

    def testRightTriangleA(self): 
        self.assertEqual(classify_triangle(3,4,5),'Right','3,4,5 is a Right triangle')
        print('Case passed: 3,4,5 is a Right triangle')

    def testRightTriangleB(self):
        self.assertEqual(classify_triangle(5,3,4),'Right','5,3,4 is a Right triangle')
        print('Case passed: 5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classify_triangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
        print('Case passed: 1,1,1 should be equilateral')

    def testIsoscelesTriangleA(self):
        self.assertEqual(classify_triangle(2,1,2),'Isoceles', '2,1,2 shold be isoceles triangle')
        print('Case passed: 2,1,2 should be isoceles triangle')

    def testScaleneTriangleA(self):
        self.assertEqual(classify_triangle(3,1,5), 'NotATriangle', '3,1,5 should not be scalene triangle')
        print('Case passed: 3,1,5 should not be scalene triangle')

    def testTriangleLengthGreaterThan200(self):
        self.assertEqual(classify_triangle(201,201,1), 'InvalidInput', '201,201,1 should not be triangle')
        print('Case passed: 201,201,1 should not be triangle')

    def testTriangeLengthForNegatoveValues(self):
        self.assertEqual(classify_triangle(-1,1,1), 'InvalidInput', '-1,1,1 should not be triangle')
        print('Case passed: -1,1,1 should not be triangle')

    def testTriangleLengthForInputString(self):
        self.assertEqual(classify_triangle('a',1,1), 'InvalidInput', 'All length sides should be numeric')
        print('Case passed: All input should be numeric')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()