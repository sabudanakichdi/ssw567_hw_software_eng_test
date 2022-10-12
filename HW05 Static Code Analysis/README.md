#Static Code Analyzer (PyLint)

#Initial PyLint Report:
*** Module Triangle ***
Triangle.py:14:91: C0303: Trailing whitespace (trailing-whitespace)
Triangle.py:15:19: C0303: Trailing whitespace (trailing-whitespace)
Triangle.py:16:0: C0303: Trailing whitespace (trailing-whitespace)
Triangle.py:19:0: C0303: Trailing whitespace (trailing-whitespace)
Triangle.py:26:0: C0303: Trailing whitespace (trailing-whitespace)
Triangle.py:30:43: C0303: Trailing whitespace (trailing-whitespace)
Triangle.py:34:0: W0301: Unnecessary semicolon (unnecessary-semicolon)
Triangle.py:39:0: C0303: Trailing whitespace (trailing-whitespace)
Triangle.py:42:0: C0303: Trailing whitespace (trailing-whitespace)
Triangle.py:43:0: C0303: Trailing whitespace (trailing-whitespace)
Triangle.py:44:59: C0303: Trailing whitespace (trailing-whitespace)
Triangle.py:50:0: C0303: Trailing whitespace (trailing-whitespace)
Triangle.py:51:47: C0303: Trailing whitespace (trailing-whitespace)
Triangle.py:54:0: C0301: Line too long (123/100) (line-too-long)
Triangle.py:1:0: C0103: Module name "Triangle" doesn't conform to snake_case naming style (invalid-name)
Triangle.py:12:0: C0103: Function name "classifyTriangle" doesn't conform to snake_case naming style (invalid-name)
Triangle.py:12:21: C0103: Argument name "a" doesn't conform to snake_case naming style (invalid-name)
Triangle.py:12:23: C0103: Argument name "b" doesn't conform to snake_case naming style (invalid-name)
Triangle.py:12:25: C0103: Argument name "c" doesn't conform to snake_case naming style (invalid-name)
Triangle.py:52:4: R1705: Unnecessary "elif" after "return", remove the leading "el" from "elif" (no-else-return)
Triangle.py:12:0: R0911: Too many return statements (8/6) (too-many-return-statements)


Report
======

Messages
--------
+---------------------------+------------+
|message id                 |occurrences |
+===========================+============+
|trailing-whitespace        |12          |
+---------------------------+------------+
|invalid-name               |5           |
+---------------------------+------------+
|unnecessary-semicolon      |1           |
+---------------------------+------------+
|too-many-return-statements |1           |
+---------------------------+------------+
|no-else-return             |1           |
+---------------------------+------------+
|line-too-long              |1           |
+---------------------------+------------+

------------------------------------------------------------------
Your code has been rated at 0.00/10 (previous run: 0.00/10, +0.00)

#Changes Done After PyLint report:
-	Removed unnecessary comments
-	Removed Multiple Trailing Whitespaces
-	Changed Function name "classifyTriangle" to “classify_triangle” to conform to snake_case naming style
-	Resolved Lines too long issue
-	Replaced all Argument name to match snake_case naming style. Replaced argument “a” with “side_1”, argument “b” with “side_2” and argument “c” with "side_3”
-	Added comment (Method Docstring) to function classify_triangle
-	Changed “elif” condition to “if” condition due to unnecessary "elif" after "return", remove the leading "el" from "elif" (no-else-return)


#After Changes Pylint Report:


*** Module Triangle ***
Triangle.py:1:0: C0103: Module name "Triangle" doesn't conform to snake_case naming style (invalid-name)
Triangle.py:8:0: R0911: Too many return statements (8/6) (too-many-return-statements)

Report
======

Messages
--------
+---------------------------+------------+
|message id                 |occurrences |
+===========================+============+
|too-many-return-statements |1           |
+---------------------------+------------+
|no-else-return             |1           |
+---------------------------+------------+
|invalid-name               |1           |
+---------------------------+------------+

------------------------------------------------------------------
Your code has been rated at 8.12/10 (previous run: 0.00/10, +8.12)