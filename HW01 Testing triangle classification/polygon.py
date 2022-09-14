class triangle():
    def __init__(self,a,b,c):
        self.s1=a
        self.s2=b
        self.s3=c

    def is_triangle (self):
        is_not_number = []
        if not isinstance(self.s1, (int, float)) or isinstance(self.s1, bool):
            is_not_number.append(self.s1)
        if not isinstance(self.s2, (int, float)) or isinstance(self.s2, bool):
            is_not_number.append(self.s1)
        if not isinstance(self.s3, (int, float)) or isinstance(self.s3, bool):
            is_not_number.append(self.s1)

        if len(is_not_number)>0:
            [print(s, type(s)) for s in is_not_number]
            raise TypeError("Value must be of type int/float")
            

