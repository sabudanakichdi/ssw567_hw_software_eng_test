# ssw567_hw_software_eng_test

# HW 02a: Testing a legacy program and reporting on testing results

# Test Run 1

| Test ID | Input | Expected Results | Actual Result | Pass or Fail | 
|---|---|---|---|---|
| testRightTriangleA | (3,4,5) | Right | InvalidInput | Fail |
| testRightTriangleB | (5,3,4) | Right | InvalidInput | Fail |
| testEquilateralTriangles | (1,1,1) |  Equilateral | InvalidInput | Fail |
| testIsoscelesTriangleA | (2,1,2) |  Isoceles | InvalidInput | Fail |
| testScaleneTriangleA | (3,1,5) |  NotATriangle | InvalidInput | Fail |
| testTriangleLengthGreaterThan200 | (201,201,1) |  InvalidInput | InvalidInput | Pass |
| testTriangeLengthForNegatoveValues | (-1,1,1) |  InvalidInput | InvalidInput | Pass |
| testTriangleLengthForInputString | ('a',1,1) |  InvalidInput | TypeError: '>' not supported between instances of 'str' and 'int' | Fail |

# Test Run 2

| Test ID | Input | Expected Results | Actual Result | Pass or Fail | 
|---|---|---|---|---|
| testRightTriangleA | (3,4,5) | Right | NotATriangle | Fail |
| testRightTriangleB | (5,3,4) | Right | NotATriangle | Fail |
| testEquilateralTriangles | (1,1,1) |  Equilateral | NotATriangle | Fail |
| testIsoscelesTriangleA | (2,1,2) |  Isoceles | NotATriangle | Fail |
| testScaleneTriangleA | (3,1,5) |  NotATriangle | NotATriangle | Pass |
| testTriangleLengthGreaterThan200 | (201,201,1) |  InvalidInput | InvalidInput | Pass |
| testTriangeLengthForNegatoveValues | (-1,1,1) |  InvalidInput | InvalidInput | Pass |
| testTriangleLengthForInputString | ('a',1,1) |  InvalidInput | InvalidInput | Pass |

# Test Run 3

| Test ID | Input | Expected Results | Actual Result | Pass or Fail | 
|---|---|---|---|---|
| testRightTriangleA | (3,4,5) | Right | NotATriangle | Fail |
| testRightTriangleB | (5,3,4) | Right | NotATriangle | Fail |
| testEquilateralTriangles | (1,1,1) |  Equilateral | Equilateral | Pass |
| testIsoscelesTriangleA | (2,1,2) |  Isoceles | Equilateral | Fail |
| testScaleneTriangleA | (3,1,5) |  NotATriangle | NotATriangle | Pass |
| testTriangleLengthGreaterThan200 | (201,201,1) |  InvalidInput | InvalidInput | Pass |
| testTriangeLengthForNegatoveValues | (-1,1,1) |  InvalidInput | InvalidInput | Pass |
| testTriangleLengthForInputString | ('a',1,1) |  InvalidInput | InvalidInput | Pass |

# Test Run 4

| Test ID | Input | Expected Results | Actual Result | Pass or Fail | 
|---|---|---|---|---|
| testRightTriangleA | (3,4,5) | Right | Right | Pass |
| testRightTriangleB | (5,3,4) | Right | Right | Pass |
| testEquilateralTriangles | (1,1,1) |  Equilateral | Equilateral | Pass |
| testIsoscelesTriangleA | (2,1,2) |  Isoceles | Isoceles | Pass |
| testScaleneTriangleA | (3,1,5) |  NotATriangle | NotATriangle | Pass |
| testTriangleLengthGreaterThan200 | (201,201,1) |  InvalidInput | InvalidInput | Pass |
| testTriangeLengthForNegatoveValues | (-1,1,1) |  InvalidInput | InvalidInput | Pass |
| testTriangleLengthForInputString | ('a',1,1) |  InvalidInput | InvalidInput | Pass |