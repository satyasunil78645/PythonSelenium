class A:
    def __init__(self):
        print("A class constructor")


    def Feature(self):
        print("feature -- 1A")


class B:
    def __init__(self):
        print("B class constructor")
        super().__init__()

    def Feature1(self):
        print("feature -- 1B")


class C(A, B):
    def __init__(self):
        print("C class constructor")



a1 = C()

a1.feature1()
