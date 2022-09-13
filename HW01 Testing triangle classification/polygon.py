class triangle():
    def __init__(self,a,b,c):
        self.s1=a
        self.s2=b
        self.s3=c

    def is_triangle (self):
        is_not_number = []
        if not isinstance(self.s1, (int, float)) and isinstance(self.s1, bool):
            is_not_number.insert(s1)
        if not isinstance(self.s2, (int, float)) and isinstance(self.s2, bool):
            is_not_number.insert(s1)
        if not isinstance(self.s3, (int, float)) and isinstance(self.s3, bool):
            is_not_number.insert(s1)

        if len(is_not_number)>0:
            print("Sides")
            [print(s) for s in is_not_number]
            print(" is not integer")
            raise ValueError("All input value needs to be Integer")
            

