# mydict= {
#     101:"ram",
#     102:"hima",
#     103:"Vidh",
#     "103":"sham",
#     "104" :"trived",
#     101:"ashish",
#     104: "guurru"

# }
#print(mydict)
#print(type(mydict))
# a=mydict[102]
# print(a)
# mydict[102]="steve"
# print(mydict)

# for x in mydict:
#     print(x)
#ans only keys

# for x in mydict.values():
#     print(x)
#ans only values

# for x,y in mydict.items():
#     print(x,y)
#ans both key and value

# mydict["mob_no"]=5678909876
# print(mydict)
# adding new key:value pair

# mydict.pop(104)
# print(mydict)

# a={(1,2):1,(2,3):2,(4,5):3}
# print(a[4,5])
# tuple as a key

# a={'a':1,'b':2,'c':3,'d':4}
# print(a['a','b'])
# keyerror

# arr={}
# arr[1]=1
# arr['1']=2
# arr[1]+=1
# #print(arr)
# sum=0
# for k in arr:
#     sum+=arr[k]
# print(sum)

# arr={}
# arr[1]=1
# arr['1']=2
# arr[1.0]=4
# print(arr)
# sum=0
# for k in arr:
#     sum+=arr[k]
# print(sum)

# mydict={}
# mydict[(1,2,4)]=8
# mydict[(4,2,1)]=10
# mydict[(1,2)]=12
# sum=0
# for k in mydict:
#     sum +=mydict[k]
# print(sum)
# print(mydict)

#Q6
# box = {}
# jars = {}
# crates = {}
# box['biscuit'] = 1
# box['cake'] = 3
# jars['jam'] = 4
# crates['box'] = box
# crates['jars'] = jars
# print(len(crates[box])) 
# this will give an error because we are trying to access the value of a key 
# that is a dictionary (box) which is not hashable and cannot be used as a key in another dictionary (crates)
# op is TypeError: unhashable type: 'dict'
#-----------------------------------------------------------------------------------------------------------------------

#Q7
# dict = {'c': 97, 'a': 96, 'b': 98}
# for _ in sorted(dict):
#     print(dict[_]) #print key and value in sorted order of keys
# # op is 96, 98, 97
#-----------------------------------------------------------------------------------------------------------------------

#Q8
# rec = {"Name": "Prashant", "Age": 25}
# r = rec.copy() # create a shallow copy of rec
# print(id(r) == id(rec)) #print False because r and rec are two different objects in memory
# # op is False
# print(id(r))
# print(id(rec))    # op is different memory addresses for r and rec
#-----------------------------------------------------------------------------------------------------------------------

#Q9
# rec = {"Name": "Python", "Age": 25, 'address': 'ngp, 'country': 'India'}
# id1 = id(rec)
# del rec
# rec = {"Name": "Python", "Age": 25, 'address': 'ngp', 'country': 'India'} 
# id2 = id(rec)
# print(id1 == id2) # this will print False because the two dictionaries are different objects in memory
# op is False
# print(id1)
# print(id2)
# op is different memory addresses for id1 and id2
#-----------------------------------------------------------------------------------------------------------------------

#Q10    finding the max value in the dictionary
# dict = {'a': 1, 'b': 2, 'c': 3}
# max_value = max(dict.values()) # maximum value
# print(max_value) # this will print the maximum value in the dictionary
# # op is 3
#-----------------------------------------------------------------------------------------------------------------------

#Q11   finding the key with the minimum value in the dictionary
# dict = {'X': 20, 'Y': 10, 'Z': 30}
# min_key = min(dict, key=dict.get)
# print(min_key) 
# # op is 'Y'
#-----------------------------------------------------------------------------------------------------------------------

#Q/ count frequency of elements in a list using dict
# mydict = [1, 2, 2, 3, 4, 3, 5]
# frequency = {}
# for item in mydict:
#     if item in frequency:
#         frequency[item] += 1  # Increment if already in dict
#     else:
#         frequency[item] = 1   # Add to dict with a count of 1
# print(frequency)

# num=123
# #print(5/2)
# #print(5//2)
# #print(num%10)
# a=num%10
# num=num//10
# b=num%10
# c=num//10
# rev = a*100 + b*10+c*1
# print(rev)


# amount=int(input("Please Enter Amount for withdraw: "))
# print("100 notes=",amount//100)
# print("50 notes=",(amount%100)//50)
# print("20 notes=",((amount%100)%50)//20)
# print("10 notes=",(((amount%100)%50)%20)//10)
# print("5 notes=",((((amount%100)%50)%20)%10)//5)
# print("2 notes=",(((((amount%100)%50)%20)%10)%5)//2)
# print("1 notes=",((((((amount%100)%50)%20)%10)%5)%2)//1)







