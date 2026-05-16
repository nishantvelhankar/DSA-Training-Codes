# class Name:
#     age=30#data member
#     def display(self):#method
#         print("hello world")
# obj = Name()
# print(obj.age)
# obj.display()

# class Student:
#     def __init__(self):
#        self.name = "Nishant" # 4 byte
#        self.age= 22          # 2 byte
    
#     def display(self):
#         print("Name = ", self.name)
#         print("Age = ", self.age)
# studobj=Student()
# print(studobj)


# class Message:
#     def __init__(self):
#        print("I am Constructor")
#     def shows(self):
#         print("Class Program")
# obj=Message()
# obj.shows()
# obj2=Message()

class StudentInfo:
    def __init__(self,name,age,roll_no):
        self.Name=name
        self.Age = age
        self.RollNo = roll_no
    
    def displayStudentInfo(self):
        print("Name= ", self.Name)
        print("Age = ", self.Age)

studentobj=StudentInfo("Nishant",22,101)
studentobj.displayStudentInfo()





