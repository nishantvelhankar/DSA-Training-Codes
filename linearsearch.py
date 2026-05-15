def linearSearch(array,target):
    for i in range(0,len(array)):#i=0
        if array[i]==target:# 0==7
            return i
    return -1

array=[1,2,3,4,8,7,9]
target = 7 # search the target value i.e 7
result=linearSearch(array,target)
if result==-1:
    print("Target value not found")
else:
    print("Target value found at index ", result)
    