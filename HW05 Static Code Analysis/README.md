# Static Code Analyzer (PyLint)

# Initial PyLint Report:
*** Module Triangle *** <br />
Triangle.py:14:91: C0303: Trailing whitespace (trailing-whitespace) <br />
Triangle.py:15:19: C0303: Trailing whitespace (trailing-whitespace) <br />
Triangle.py:16:0: C0303: Trailing whitespace (trailing-whitespace) <br />
Triangle.py:19:0: C0303: Trailing whitespace (trailing-whitespace) <br />
Triangle.py:26:0: C0303: Trailing whitespace (trailing-whitespace) <br />
Triangle.py:30:43: C0303: Trailing whitespace (trailing-whitespace) <br />
Triangle.py:34:0: W0301: Unnecessary semicolon (unnecessary-semicolon) <br />
Triangle.py:39:0: C0303: Trailing whitespace (trailing-whitespace) <br />
Triangle.py:42:0: C0303: Trailing whitespace (trailing-whitespace) <br />
Triangle.py:43:0: C0303: Trailing whitespace (trailing-whitespace) <br />
Triangle.py:44:59: C0303: Trailing whitespace (trailing-whitespace) <br />
Triangle.py:50:0: C0303: Trailing whitespace (trailing-whitespace) <br />
Triangle.py:51:47: C0303: Trailing whitespace (trailing-whitespace) <br />
Triangle.py:54:0: C0301: Line too long (123/100) (line-too-long) <br />
Triangle.py:1:0: C0103: Module name "Triangle" doesn't conform to snake_case naming style (invalid-name) <br />
Triangle.py:12:0: C0103: Function name "classifyTriangle" doesn't conform to snake_case naming style (invalid-name) <br />
Triangle.py:12:21: C0103: Argument name "a" doesn't conform to snake_case naming style (invalid-name) <br />
Triangle.py:12:23: C0103: Argument name "b" doesn't conform to snake_case naming style (invalid-name) <br />
Triangle.py:12:25: C0103: Argument name "c" doesn't conform to snake_case naming style (invalid-name) <br />
Triangle.py:52:4: R1705: Unnecessary "elif" after "return", remove the leading "el" from "elif" (no-else-return) <br />
Triangle.py:12:0: R0911: Too many return statements (8/6) (too-many-return-statements) <br />


Report
======

Messages
--------
+---------------------------+------------+ <br />
|message id                 |occurrences | <br />
+===========================+============+ <br />
|trailing-whitespace        |12          | <br />
+---------------------------+------------+ <br />
|invalid-name               |5           | <br />
+---------------------------+------------+ <br />
|unnecessary-semicolon      |1           | <br />
+---------------------------+------------+ <br />
|too-many-return-statements |1           | <br />
+---------------------------+------------+ <br />
|no-else-return             |1           | <br />
+---------------------------+------------+ <br />
|line-too-long              |1           | <br />
+---------------------------+------------+ <br />

------------------------------------------------------------------
Your code has been rated at 0.00/10 (previous run: 0.00/10, +0.00)

# Changes Done After PyLint report:
-	Removed unnecessary comments
-	Removed Multiple Trailing Whitespaces
-	Changed Function name "classifyTriangle" to �classify_triangle� to conform to snake_case naming style
-	Resolved Lines too long issue
-	Replaced all Argument name to match snake_case naming style. Replaced argument �a� with �side_1�, argument �b� with �side_2� and argument �c� with "side_3�
-	Added comment (Method Docstring) to function classify_triangle
-	Changed �elif� condition to �if� condition due to unnecessary "elif" after "return", remove the leading "el" from "elif" (no-else-return)


# After Changes Pylint Report:


*** Module Triangle *** <br />
Triangle.py:1:0: C0103: Module name "Triangle" doesn't conform to snake_case naming style (invalid-name) <br />
Triangle.py:8:0: R0911: Too many return statements (8/6) (too-many-return-statements) <br />

Report
======

Messages
--------
+---------------------------+------------+ <br />
|message id                 |occurrences | <br />
+===========================+============+ <br />
|too-many-return-statements |1           | <br />
+---------------------------+------------+ <br />
|no-else-return             |1           | <br />
+---------------------------+------------+ <br />
|invalid-name               |1           | <br />
+---------------------------+------------+ <br />

------------------------------------------------------------------
Your code has been rated at 8.12/10 (previous run: 0.00/10, +8.12)

# Code Coverage
|Name            | Stmts  | Miss | Cover | Missing |
|-|-|-|-|-| 
|TestTriangle.py  |   31   |  0  | 100% |  |
|Triangle.py      |    17   |   1  |  94% |  29 |
|-|-|-|-|-|
|TOTAL            |    48  |    1  |  98% |