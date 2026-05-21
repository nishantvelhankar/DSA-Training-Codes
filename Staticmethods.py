class Student:
    @staticmethod
    def get_personal_detail(firstname,lastname):
        print("Your personal detail", firstname,lastname)
    @staticmethod
    def contact_detail(mobno,roll_no):
        print(" your contact detail : ", mobno,roll_no)
Student.get_personal_detail("Nishant" ,"Velhankar")
Student.contact_detail(8634567890,21)