class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self, a, b):
        s = a + b
        print(s)
        return s


s1 = Student(10, 13)

s1.sum(1, 2)
