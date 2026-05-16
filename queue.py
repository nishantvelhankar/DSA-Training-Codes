# import sys
# class Queue:
#     def __init__(self,size):
#         self.myqueue=[]
#         self.queuesize = size
#     def isfull(self):
#        if len(self.myqueue)==size:
#           return True
#        else:
#           return False
#     def enqueue(self,values):
#        if self.isfull():
#           print("Queue is full")
#        else:
#           self.myqueue.append(value)
#     def display(self):
#        print(self.myqueue)
#     def isempty(self):
#         if self.myqueue==[]:
#            return True
#         else:
#            return False
#     def dequeue(self):
#        if self.isempty():
#           print("Queue is Empty")
#        else:
#           self.myqueue.pop(0)
#     def peek(self):
#        if self.isempty():
#           print("Queue is Empty")
#        else:
#           print(self.myqueue[0])
#     def deletequeue(self):
#        self.myqueue=None

# size=int(input("Enter the size : "))     
# obj=Queue(size)
# print("Queue has Created: ")
# while True:
#    print("1.Enqueue Operation")
#    print("2. Display Queue")
#    print("3. Dequeue Operation")
#    print("4. Peek Operation")
#    print("5. Delete Queue Operation")
#    print("6. Exit")

#    choice=int(input("Enter your choice: "))
#    if choice ==1:
#       value = int(input("Enter value to add in Queue: "))
#       obj.enqueue(value)
#    elif choice==2:
#       obj.display()
#    elif choice == 3:
#       obj.dequeue()
#    elif choice == 4:
#       obj.peek()
#    elif choice == 5:
#       obj.deletequeue() 
#    else:
#       sys.exit()



# interview question

# stack using list
# - easy to implement
# - speed problem when it grows

# stack using linkedlist
# - fast performance
# - implementation is not easy

# queue using list
# - easy to implement
# - speed problem when it grows

# queue using linked list
# fast performance
# implementation not easy

# fruits ={}
# def addone(index):
#     if index in fruits:
#         fruits[index]+=1
#     else:
#         fruits[index]=1

# addone('Apple')
# addone('Banana')
# addone('apple')
# print(len(fruits))

# problem:

# students = {}
# n = int(input("How many students:  "))
# for i in range(n):
#     name = input("Enter student name: ")
#     marks = int(input("Enter marks: "))
#     students[name] = marks
# search_name = input("Enter student name to search: ")
# if search_name in students:
#     print("Marks =", students[search_name])
# else:
#     print("Student not found")



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


# v=['a','e','i','o','u']
# w = input("Enter the word where we will search the vowels: ")
# found=[]
# for i in w :
#     if i in v:
#         if i not in found:
#             found.append(i)
# print("Found vowels = ", found)
# print("Unique vowels",len(found),'from given word= ', w)





