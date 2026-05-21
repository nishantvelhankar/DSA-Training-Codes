# single linked list: 
# class College:
#     def college_name(self):
#         print("Modern college")

# class Student(College):
#     def student_info(self):
#        print("Name:","Nishant")
#        print("Branch: ","MCA")
# obj=Student()
# obj.college_name()
# obj.student_info()


class College:
    def college_name(self):
        print("Modern college")

class Student(College):
    def student_info(self):
       print("Name:","Nishant")
       print("Branch: ","MCA")

class Exam(Student):
    def subject(self):
        print("Subject1: Design EnG")
        print("Subject2: math")
        print("Subject3: python")

obj=Exam()
obj.college_name()
obj.student_info()
obj.subject()

