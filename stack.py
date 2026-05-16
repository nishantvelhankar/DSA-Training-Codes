# import sys
# class Stack:
#     def __init__(self):
#      self.myStack =[] #creating stack

#     def push(self,value):
#        self.myStack.append(value)
#        print("Element pushed")

#     def displaystack(self):
#        print(self.myStack)

#     def isempty(self):
#        if self.myStack==[]:
#           return True
#        else:
#           return False
       
#     def pop(self):
#        if self.isempty():
#           print("stack is empty")
#        else:
#           print(self.myStack.pop())  
#     def peek(self):# topmost element return
#        if self.isempty():
#           print("Stack is Empty")
#        else:
#           print(self.myStack[-1])
#     def deletestack(self):
#        self.myStack=[]
#        print("Stack deleted")
       
# obj=Stack()
# print("Stack has Created: ")
# while True:
#    print("1.Push Operation")
#    print("2. Display Stack")
#    print("3. Pop Operation")
#    print("4. Peek Operation")
#    print("5. Delete stack Operation")
#    print("7. Exit")

#    choice=int(input("Enter your choice: "))
#    if choice ==1:
#       value = int(input("Enter value to push in stack: "))
#       obj.push(value)
#    elif choice==2:
#       obj.displaystack()
#    elif choice == 3:
#       obj.pop()
#    elif choice == 4:
#       obj.peek()
#    elif choice == 5:
#       obj.deletestack()
#    else:
#       sys.exit()


import sys
class Stack:
    def __init__(self,size):
     self.myStack =[] #creating stack
     self.stacksize=size
    def isfull(self):
       if len(self.myStack)==self.stacksize:
          return True
       else:
          return False

    def push(self,value):
       if self.isfull():
          print("full")
       else:
        self.myStack.append(value)
        print("Element pushed")

    def displaystack(self):
       print(self.myStack)

    def isempty(self):
       if self.myStack==[]:
          return True
       else:
          return False
       
    def pop(self):
       if self.isempty():
          print("stack is empty")
       else:
          print(self.myStack.pop())  
    def peek(self):# topmost element return
       if self.isempty():
          print("Stack is Empty")
       else:
          print(self.myStack[-1])
    def deletestack(self):
       self.myStack=[]
       print("Stack deleted")

size=int(input("Enter the size : "))     
obj=Stack(size)
print("Stack has Created: ")
while True:
   print("1.Push Operation")
   print("2. Display Stack")
   print("3. Pop Operation")
   print("4. Peek Operation")
   print("5. Delete stack Operation")
   print("7. Exit")

   choice=int(input("Enter your choice: "))
   if choice ==1:
      value = int(input("Enter value to push in stack: "))
      obj.push(value)
   elif choice==2:
      obj.displaystack()
   elif choice == 3:
      obj.pop()
   elif choice == 4:
      obj.peek()
   elif choice == 5:
      obj.deletestack()
   else:
      sys.exit()
