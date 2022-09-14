from triangleClassifier import triangleClassifierCl as tc
import unittest as u

class testTriangleClassifier(u.TestCase):
    def test_init(self):
        print("Start Test init")
        a=1
        b=2
        c=3
        t = tc(a,b,c)
        self.assertEqual(t.s1,a)
        self.assertEqual(t.s2,b)
        self.assertEqual(t.s3,c)
        print("Test init Complete")

    def test_null_args_init(self):
        print("Start Test null args init")
        with self.assertRaises(TypeError) as ex:
            tc()
        print("Caught Exeception ", str(ex.exception))
        print("Test null args init Completed")

    def test_two_args_init(self):
        print("Start Test two args init")
        with self.assertRaises(TypeError) as ex:
            tc(1,2)
        print("Caught Exeception ", str(ex.exception))
        print("Test two args init Completed")

    def test_right_angle(self):
        print("Start Test Right Angle")
        t = tc(3,4,5)
        self.assertTrue(t.is_right_angled_triangle())
        self.assertFalse(tc(4,6,7).is_right_angled_triangle())
        print("Test Right Angle Complete")

    def test_equilateral_triangle(self):
        print("Start Test Equilateral Triangle")
        t = tc(3,3,3)
        self.assertTrue(t.is_equilateral())
        self.assertFalse(tc(1,2,3).is_equilateral())
        print("Test Equilateral Triangle Complete")

    def test_isosceles_triangle(self):
        print("Start Test Isosceles Triangle")
        t = tc(2,1,3)
        self.assertFalse(t.is_isosceles())
        self.assertTrue(tc(2,2,1).is_isosceles())
        print("Test Isosceles Triangle Complete")

    def test_scalene_triangle(self):
        print("Start Test Scalene Triangle")
        a = True
        t = tc(7,8,9)
        self.assertEqual(t.type_of_triangle(), a)
        self.assertFalse(tc(1,1,2).type_of_triangle())
        print("Test Scalene Triangle Complete")
        
    def test_Exception_TypeError(self):
        print("Start Test Exception Type Error")
        t = tc("abc",2,3)
        with self.assertRaises(TypeError):
            t.is_triangle()
        print("Test Exception Type Error Complete")

if __name__ == 'main':
    u.main()

