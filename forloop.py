# for and while loops are entry points to iteration in Python. They allow you to execute a block of code repeatedly.
#for(initialization; condition; increment/decrement):
# for i in range(5):
#     print(i)
# for i in range(2,10):
#  print(i)
# for i in range(2,10,2):
#     print(i)
# print("---------------------------------------------------")
# for i in range(5,0,-1):
#     print(i)
# print("---------------------------------------------------")
# for i in range(1,11):
#     print(i*2)

# problem statement: tables from 2 to 20

# for i in range(1,11):
#     print(i*2,"",i*3," ",i*4," ",i*5," ",i*6," ",i*7," ",i*8," ",i*9," ",i*10)  
# print("----------------------------------------------------------------------------------------------")
# for i in range(1,11):
#     print(i*11,"",i*12," ",i*13," ",i*14," ",i*15," ",i*16," ",i*17," ",i*18," ",i*19," ",i*20)


# problem statement: wap to accept where paper marks and calculate the total, percentage and check if he/she is passed in all the subject so print pass else print fail.
# math=50
# chem=60
# phy=69
# total=math+chem+phy
# percentage=total/3
# print("Percentage:",percentage)
# if math>=35 and chem>=35 and phy>=35:
#     print("Total marks:",total)
#     print("Pass")
# else:   
#     print("Total marks:",total)
#     print("Fail")

# # problem statement: if percentage is greater than or equal to 65 print and gender ="male" so he is eligible placement else not eligible.
# gender="male"
# if percentage>=65 and gender=="male":
#     print("Eligible for placement")
# else:
#     print("Not eligible for placement")



#problem statement: 1245 5421
#zip() we can take multiple range functions inside zip().
# for i,j in zip(range(1,6),range(5,0,-1)):
#  if i==3 and j==3:
#    continue
#  print(i," ",j)
