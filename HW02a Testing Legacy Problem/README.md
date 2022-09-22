# ssw567_hw_software_eng_test

# HW 02a: Testing a legacy program and reporting on testing results

# Test Run 1

| Test ID | Input | Expected Results | Actual Result | Pass or Fail | 
|---|---|---|---|---|
| testRightTriangleA | (3,4,5) | Right | InvalidInput | Fail |
| testRightTriangleB | (5,3,4) | Right | InvalidInput | Fail |
| testEquilateralTriangles | (1,1,1) |  Equilateral | InvalidInput | Fail |
| testIsoscelesTriangleA | (1,1,2) |  Isoceles | InvalidInput | Fail |
| testScaleneTriangleA | (3,1,5) |  Scalene | InvalidInput | Fail |
| testTriangleLengthGreaterThan200 | (201,201,1) |  InvalidInput | InvalidInput | Pass |
| testTriangeLengthForNegatoveValues | (-1,1,1) |  InvalidInput | InvalidInput | Pass |
| testTriangleLengthForInputString | ('a',1,1) |  InvalidInput | TypeError: '>' not supported between instances of 'str' and 'int' | Fail |

# Test Run 2

| Test ID | Input | Expected Results | Actual Result | Pass or Fail | 
|---|---|---|---|---|
| testRightTriangleA | (3,4,5) | Right | NotATriangle | Fail |
| testRightTriangleB | (5,3,4) | Right | NotATriangle | Fail |
| testEquilateralTriangles | (1,1,1) |  Equilateral | NotATriangle | Fail |
| testIsoscelesTriangleA | (1,1,2) |  Isoceles | NotATriangle | Fail |
| testScaleneTriangleA | (3,1,5) |  Scalene | NotATriangle | Fail |
| testTriangleLengthGreaterThan200 | (201,201,1) |  InvalidInput | InvalidInput | Pass |
| testTriangeLengthForNegatoveValues | (-1,1,1) |  InvalidInput | InvalidInput | Pass |
| testTriangleLengthForInputString | ('a',1,1) |  InvalidInput | InvalidInput | Pass |