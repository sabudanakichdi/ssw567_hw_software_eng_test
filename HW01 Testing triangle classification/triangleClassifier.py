from polygon import triangle as t

class triangleClassifier(t):
    def __init__(self,a,b,c):
        t.__init__(self,a,b,c)

    def is_equilateral (self):
        return self.s1 == self.s2 and self.s2 == self.s3

    def is_isosceles (self):
        if (self.s1 == self.s2 and self.s2 != self.s3) or (self.s2 == self.s3 and self.s3 != self.s1) or (self.s1 == self.s3 and self.s2 != self.s3):
            return True

    def is_right_angled_triangle (self):
        return round(((self.s1**2) + (self.s2**2)),2) == round((self.s3**2), 2)

    def type_of_triangle (self):
        try:
            self.is_triangle()
            is_right = self.is_right_angled_triangle()
            print ("Right Angled Triangle")
            if self.is_equilateral():
                print ("Equilateral Triangle")
            elif self.is_isosceles():
                print ("Isosceles Triangle")
            else:
                print ("Scalene Triangle")

        except ValueError:
            print("ValueError: All input value needs to be Integer")

if __name__ == '__main__':
    c = triangleClassifier(1,2,3)
    c.type_of_triangle()
    triangleClassifier(3,4,5).type_of_triangle()
    triangleClassifier('abc',4,5).type_of_triangle()


    