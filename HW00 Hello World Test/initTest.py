from pickle import FALSE, TRUE
import unittest as u
import helloWorld as h

class initTest(u.TestCase):

    def testHelloAsTrueCondition(self):
        self.assertTrue(bool(h.init_func(1)))
        print("Test sucessful for value TRUE")

    def testHelloAsFalseCondition(self):
        self.assertEqual(h.init_func(0), 0)
        print("Test successful for value FALSE")

    def testHelloCheckException(self):
        self.assertRaises(Exception, h.except_func)
        print("Test successful for caught Exception")

    def testHelloForAssertionError(self):
        try: self.assertEqual(h.init_func(0), 1)
        except AssertionError:
            print("Test successful for Assertion Error")        

if __name__ == '__main__':
    h.hello_func()
    u.main()