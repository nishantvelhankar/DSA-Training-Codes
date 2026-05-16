import time

class Tower:

    def __init__(self):
        print("Welcome to Tower of Hanoi Game\n")

        print("Given Problem")
        print("A = [3,2,1]    B = []    C = []\n")

        print("Expected Output")
        print("A = []    B = []    C = [3,2,1]\n")

        self.A = []
        self.B = []
        self.C = []

    def tower(self, item):
        self.A.append(item)
        time.sleep(2)

        print("A =", self.A)
        print("Items inserted in Tower A\n")

    def display(self, msg):
        print(msg)
        print("A =", self.A, "   B =", self.B, "   C =", self.C)
        print("====================================\n")
        time.sleep(2)

    def pass1(self):
        temp = self.A.pop()
        self.C.append(temp)
        self.display("Pass 1 Completed")

    # Pass 2
    def pass2(self):
        temp = self.A.pop()
        self.B.append(temp)
        self.display("Pass 2 Completed")

    # Pass 3
    def pass3(self):
        temp = self.C.pop()
        self.B.append(temp)
        self.display("Pass 3 Completed")

    
    def pass4(self):
        temp = self.A.pop()
        self.C.append(temp)
        self.display("Pass 4 Completed")

    def pass5(self):
        temp = self.B.pop()
        self.A.append(temp)
        self.display("Pass 5 Completed")

    def pass6(self):
        temp = self.B.pop()
        self.C.append(temp)
        self.display("Pass 6 Completed")

    def pass7(self):
        temp = self.A.pop()
        self.C.append(temp)
        self.display("Pass 7 Completed")


obj = Tower()
obj.tower(3)
obj.tower(2)
obj.tower(1)
obj.pass1()
obj.pass2()
obj.pass3()
obj.pass4()
obj.pass5()
obj.pass6()
obj.pass7() 
