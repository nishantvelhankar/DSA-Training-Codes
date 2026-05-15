
# def hello():# called function
#      print("Hello World")
# hello()# calling function
# hello()

# def arithmatic():
#     a= int(input("Enter Value of a: "))
#     b= int(input("Enter Value of b: "))
#     sum=a+b
#     sub=a-b
#     mul=a*b
#     div=a/b
#     return sum,sub,div,mul
# # print(arithmatic())
# result=arithmatic()
# print("Arithmatic: ",result)

# how many types of arguments we pass in the function
# 1. positional arguments
# 2. keyword arguments
# 3. variable length arguments/variable number argument


# Positional argument
# def arithmatic(a,b):
#    # a= int(input("Enter Value of a: "))
#     #b= int(input("Enter Value of b: "))
#     sum=a+b
#     sub=a-b
#     mul=a*b
#     div=a/b
#     return sum,sub,div,mul
# # print(arithmatic())
# result=arithmatic(5,5)
# print("Arithmatic: ",result)

#keyword argument
# def credential(username,password):
#     if username==password:
#         print("Login successfully")
#     else:
#         print("invalid credentials")
# credential(username='admin',password='admin')#calling function


# default argument
# def cityname(city='pune'):
#     print(city)
# cityname("Nagpur")
# cityname("Mumbai")
# cityname()

#variable length argument
# def cityname(*name):
#     print(name)
# cityname("Nagpur","Mumbai","Pune")

#modularity approach in function
# import sys
# def add():
#     a=int(input("Enter value of A: "))
#     b=int(input("Enter value of B: "))
#     print(a+b)

# def sub():
#     a=int(input("Enter value of A: "))
#     b=int(input("Enter value of B: "))
#     print(a-b)


# def mul():
#     a=int(input("Enter value of A: "))
#     b=int(input("Enter value of B: "))
#     print(a*b)

# def div():
#     a=int(input("Enter value of A: "))
#     b=int(input("Enter value of B: "))
#     print(a/b)

# while(True):
#     print("1.Add")
#     print("2.Sub")
#     print("3.Mul")
#     print("4.Div")
#     print("5.exit")
#     choice=int(input("Enter Your Choice: "))
#     if choice == 1:
#         add()
#     elif choice ==2:
#         sub()
#     elif choice == 3:
#         mul()
#     elif choice == 4:
#         div()
#     elif choice == 5:
#         sys.exit()







