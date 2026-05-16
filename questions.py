#wipro questions
# import math
# noOfPlot = int(input("Enter the no. of plot: "))
# plots = input("Enter plots(space separated): ")
# list  = []
# for i in plots.split():
#     root = math.sqrt(int(i))
#     if root == int(root):
#         list.append(int(i))

# print("Total eligible plots = ",len(list))


# def func(value,values):
#  var=1
#  values[0]=44
# t= 3
# v = [1,2,3]
# func(t,v)
# print(t,v[0])

# def f(i,values=[]):
#     values.append(i)
#     print(values)
#     # return values
# f(1)
# f(2)
# f(3)



# s = "Learning Python is very easy"
# n = len(s)
# print("Forward direction:")
# i = 0
# while i < n:
#     print(s[i], end="")
#     i += 1
# print("\n\nBackward direction:")
# i = n - 1
# while i >= 0:
#     print(s[i], end="")
#     i -= 1


# # problem :
# x,y,z = map(int,(input().split()))
# mylist=[]
# for i in range(x):
#     a=int(input())
#     mylist.append(a)
# for j in mylist:
#     if j>=y and j<=z:
#         print(j,end=' ')


# import datetime
# date = datetime.datetime.now()
# print("It's now : {:%d/%m/%Y:%H:%M:%S}".format(date))


# x=['A','B','C']
# y=['A','B','C']
# z=[1,2,3,4]
# print(x==y)
# print(x==z)
# print(x!=z)

#list comprehension
#s=[1,4,9,16,25,36,49,64,81,100]
# val=[2**i for i in range(1,6)]
# print(val)

#dict comprehension
# square={x:x*x for x in range(1,6)}
# print(square)

# how to read multiple values from the keybord in a single line
# a,b=[int(x)for x in input("Enter 2 numberS : ").split()]
# print("Produt is : ", a*b)

# we can use else with for as well
# for --------
  #------------
#else:
#---------------------


while True:
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    if username=='admin'and password=='admin':
        print('login sucessfull')
        break
    else: 
        print("Wrong credentials. try again..")

