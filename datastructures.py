# data structures are different way of organizing data on your computer that can be used effectively.

# two steps
#1.correctness
#2.efficiency

# constant time:
# a=[1,2,3,4,5]
# a[0]# it takes constant time to access first element or any element in the array.

# linear time(traversing)
# a=[1,2,3,4]
# for element in a:
#     print(element)
# linear time since it is visiting every element of array 
# time complexity O^n


# 0(logN) logarithmic time
# a=[1,2,3,4,5]
# for index in range(0,len(array),3):
#     print(array[index])
# logarithmic time since it is visiting only some elements
#example binary search


# O(N^2) Quadratic time
# a= [1,2,3,4]
# for i in a:
#     for y in a:
#         print()
# looking at every index in array twice

#O(2^n) exponential time
# def fibonacci():
     # if n<=i:
        # return()
# return fibonacci (n-1)+ fibonacci(n-2)
# double recursion in fibonacci


# def findbiggestNumber(samplearray):#[5,7,9,2,3,4]
#     biggestnumber=samplearray[0]#biggestnumber=9 ===================> O(1)
#     for index in range(1,len(samplearray)):#index = 2 =============> O(N)
#         if samplearray[index]>biggestnumber:#9>2  ===============>O(1)
#             biggestnumber=samplearray[index] # ==================>O(1)
#     print(biggestnumber) # =====================================> O(1)

# samplearray=[5,7,9,2,3,4]
# findbiggestNumber(samplearray)

#==============================================================================
# final time complexity ======> O(1) + O(1)+ O(1) + O(1) + O(N) = O(N)


# removing spaces from string
#1.rstrip()==> to remove spaces at right hand side
#2.lstrip()==> to remove spaces at left hand side
#3.strip()==>  to removes spaces from both sides


# city=input("Enter your city name: ")
# scity=city.strip()
# if scity == "Hydrabad":
#     print("HEllO Hydrabad")
# elif scity == "Nagpur":
#     print("Hello Nagpur")
# elif scity == "Mumbai":
#     print("Hello Mumbai")
# else:
#     print("Your Entered city is invalid")
         

# row wise max value
# mylist=[[100,198,333,323],
#         [122,232,221,111],
#         [223,565,245,764]]
# newlist=[]
# for i in range(3):
#     j=0
#     max=mylist[i][j]
#     for j in range(4):
#         c_max=mylist[i][j]
#         if max < c_max:
#             max=c_max
#     newlist.append(max)
# print(newlist)

# input=nishant*is*great*programmer
#output=***nishantisgreatprorammer

# name="nishant*is*great*programmer"
# newname=''
# val=''
# for i in name:
#     if i!="*":
#         newname+=i
#     else:
#         val+=i
# print(newname)
# print(str(val+newname))


#input=aaabbbbccceeeee
#output=a3b4c3e5

def run_length_encoding(s):
    if not s:
        return ""

    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(f"{s[i - 1]}{count}")
            count = 1
    result.append(f"{s[-1]}{count}")
    return "".join(result)

input_str = "aaabbbbccceeeee"
output_str = run_length_encoding(input_str)

print(f"Input:  {input_str}")
print(f"Output: {output_str}")
