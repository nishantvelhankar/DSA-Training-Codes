# uses stack
# not memory efficient
# iteration is space efficient
# less time efficient

# when to use recursion?
# when the main problem can be divided into similar sub-problem, then we use recursion.

# def fact(i):
#     if i <=1:
#         return 1
#     return i*fact(i-1)
# print(fact(4))


# capatalize problem using recursion

# def capitalize(arr):
#     result=[]
#     if len(arr)==0:
#         return result
#     result.append(arr[0][0].upper() + arr[0][1:])
#     return result + capitalize(arr[1:])
# print(capitalize(['car','taco','banana']))


# def power(base,exponent):
#     if exponent==0:
#         return 1
#     return base * power(base,exponent-1)
# print(power(2,0))
# print(power(2,2))
# print(power(2,4))


# def productofarray(arr):
#     if len(arr)==0:
#         return 1
#     return arr[0]*productofarray(arr[1:])
# print(productofarray([1,2,3]))
# print(productofarray([1,2,3,10]))

# reverse string using recursion
# def reverse(string):
#     if len(string)<=1:
#         return string
#     return string[len(string)-1]+ reverse(string[0:len(string)-1])
# print(reverse("python"))


# def recursiverange(num):
#     if num<=0:
#         return 0
#     return num +recursiverange(num-1)
# print(recursiverange(6))

# def ispalindrome(string):
#     if len(string)==0:
#         return True
#     if string[0]!=string[len(string)-1]:
#         return False
#     return ispalindrome(string[1:-1])
# print(ispalindrome("awesome"))
# print(ispalindrome("tacocat"))



# somerecursive solution:
def somerecursive(arr,cb):
    if len(arr)==0:
        return False
    if not(cb(arr[0])):
        return somerecursive(arr[1:],cb)
    return True

def isodd(num):
    if num%2==0:
        return False
    else:
        return True
    
print(somerecursive([1,2,3,4],isodd))
print(somerecursive([4,6,8,9],isodd))
print(somerecursive([4,6,8],isodd))





