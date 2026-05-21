#remove leading zeros from a list of integers
# def remzerosright(arr):
#     i=0
#     while i<len(arr) and i==arr[0]:
#         arr.pop(0)
#     return arr
   
# arr=[0,0,1,2,4,0,5,0]
# print(remzerosright(arr))



# Find the first Missing Positive Integer:

# def missingposi():
#   i=0
#   while i<len(arr)and i==arr[0]:
#     arr.insert(i)


# arr=[3,4,-1,-1]
# print(missingposi(arr))

#exception handling
# import logging
# logging.basicConfig(filename='newlog.txt',level=logging.DEBUG)
# try:
#    a = int(input("Enter first number : " ))
#    b = int(input("Enter second number: "))
#    print(a/b)
# except ZeroDivisionError:
#    print("we cant divide by zero")
# except ValueError :
#    print("Enter only integer value")
# except:
#    print('404 Not found')
# finally:
#    print(" I always execute")

# except(ZeroDivisionError,ValueError) as msg:
#    print(msg)
#    logging.exception(msg)
# print("logging level is set up.Check 'newlog.txt' for log details . " )

# import csv
# f=open("employee.csv",'a')
# a=csv.writer(f)
# # a.writerow(["EmpID","Emp Name","Emp Age"])
# empid=int(input("Enter your EmpID : "))
# empname=str(input("Enter your Name : "))
# age=int(input("Enter your Age : "))
# a.writerow([empid,empname,age])
# print("file has Created")
import csv
f=open("student.csv",'a')
a=csv.writer(f)
a.writerow(["StdID","Student Name","Phy","chem","math","total","Percentage","Result"])
# stdid=int(input("Enter your EmpID : "))
# stdname=str(input("Enter your Name : "))
# phymarks=int(input("Enter your  phy marks : "))
# chemmarks=int(input("Enter your  chem marks : "))
# mathmarks=int(input("Enter your  math marks : "))
# a.writerow([stdid,stdname,phymarks,chemmarks,mathmarks])
print("file has Created")
