#mylist=['Nishant','Rohit',89,'Satyarth',65,'Shivam',93,'Satyarth',6,'Chigga',77]
# print(mylist)
# print(type(mylist))  # <class 'list'>   
# print(mylist[0])  # Nishant
# print(mylist[1])  # Rohit
# print(mylist[2])  # 89
# print(mylist[-1])  # 77
# print(mylist[:5])
# print(mylist[5:])
# print(mylist[2:7])
# print(mylist[::2])  # ['Nishant', 89, 65, 'Shivam', 'Satyarth', 77]
# print(mylist[1::2])  # ['Rohit', 'Satyarth', 'Shivam', 6, 'Shivam']
# print(mylist[::-1])  # [77, 'Shivam', 6, 'Satyarth', 93, 'Shivam', 65, 89, 'Rohit', 'Nishant']
# print(mylist[1:8:2])  # ['Rohit', 89, 'Satyarth', 93]
# mylist[2]="Kamlesh"
# print(mylist)

# if "Chigga" in mylist:
#     print("Chigga is present in the list")  
# else:    
#     print("Chigga is not present in the list")

# mylist.append("Bablesh")
# mylist.append("laxman")
# print(mylist)
# append() and extend() both work like same but append() adds a single element to the end of the list, while extend() adds multiple elements from another iterable (like another list) to the end of the list.

# to add element at specifi index we can use insert() method
# mylist.insert(2,"bhuvan")
# print(mylist)

# to remove element from list we can use remove() method
# mylist.remove("Satyarth")
# print(mylist)

# to clone a list we can use copy() method
# mylist2=mylist.copy()
# print(mylist2)


# mylist=[['Nishant','Rohit',89],['Satyarth',65,'Shivam'],['Satyarth',6,'Chigga',77]]
# print(mylist)
# #print(mylist[row][column])  # to access element from nested list we can use this syntax
# print(mylist[0][0])  # Nishant
# print(mylist[1][2])  # Shivam
# print(mylist[2][3])  # 77
# print(mylist[2][2])  # Chigga

# list2=[1,2,3,4,5,'nishant']
#del list2
#print(list2)  # NameError: name 'list2' is not defined, because we have deleted the list2 variable using del statement.
# del list2[2]
# print(list2)
# list2.clear()
# print(list2)  # [] , because clear() method removes all the elements from the list


# name="Nishant"
# print(name)
# myname=list(name)
# print(myname)  # ['N', 'i', 's', 'h', 'a', 'n', 't'] , because list() function converts the string into a list of characters


## sorting a list
# mylist=[5,2,9,1,5,6]
# #mylist.sort()  # sort() method sorts the list in ascending order by default 
# mylist.sort(reverse=True)  # sort() method with reverse=True sorts the list in descending order 
# print(mylist)  # [1, 2, 5, 5, 6, 9]
### default sorting order is ascending order,default sorting order for string is alphbetial order we should know that list should contain homogeneous data type for sorting otherwise it will give error because it cannot compare different data types. For example if we have a list with both integers and strings then it will give error because it cannot compare integer with string. So we should have a list with homogeneous data type for sorting. 

# alising means assigning a new name to an existing object. In python, when we assign a list to a new variable, it creates a reference to the same list in memory. So if we modify the list using the new variable, it will also modify the original list because both variables are referencing the same list in memory. This is called aliasing.
# mylist=[5,2,9,1,5,6]
# newlist=mylist
# print(id(mylist))  # 140353678901824
# print(id(newlist))  # 140353678901824, because both variables are referencing the same list in memory


# mylist=[4,2,9,1,7,6]
# for i in mylist:
#     print(i)


#input=[0,1,4,0,2,5]
#output=[1,4,2,5,0,0]

# for i in input:
#     if i==0:
#         input.remove(i)
#         input.append(i)
# print(input)

#find the second largest element in the list
# mylist=[7,3,9,2,8]
# mylist.sort()
# print(mylist)
# print(mylist[-2])#8

#problem statement:
# a=[1,2,3,4,5,6,7,8,9]
# a[::2]=10,20,30,40,50,60 # value error
# print(a)

#problem Statement: 
# a= [1,2,3,4,5]
# print(a[3:0:-1])

# arr=[1,2,3,4,5,6]
# for i in range (1,6): #i=1
#  arr[i-1]=arr[i]#a[0]=a[1]

# for i in range (0,6):
#     print(arr[i],end=" ")


# fruits_list1=["apple","berry","cherry","grapes","mango"]
# fruits_list2=fruits_list1
# fruits_list3=fruits_list1[:]
# fruits_list2[0]="Guava"
# fruits_list3[1]="Kiwi"

# sum=0
# for i in (fruits_list3,fruits_list2,fruits_list3):
#     if i[0]=="Guava":
#         sum+=1
#     if i[1]=="Kiwi":
#         sum+=20 
# print(sum)


#find the common elements in three arrays
#input=[[1,2,3], [2,3,4], [3,4,5]]
# A=[1,2,3]
# B=[2,3,4]
# C=[3,4,5]
# for i in A:
#     if i in B and i in C:
#         print(i)

# mylist=[]
# N = int(input("Enter the value of N: "))
# for _ in range(N):
#     val=int(input("Enter the value: "))
#     mylist.append(val)
# sum=0
# for i in range(len(mylist)-1):
#     if i+1 in range(len(mylist)):
#         sum+=abs(mylist[i]-mylist[i+1])
# print(sum)