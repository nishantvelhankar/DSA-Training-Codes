# every node is connected with head node and everytime it is disconnected when we add new node using stack implementation
# import sys

# class Node:
#     def __init__(self,data=None):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def __iter__(self):
#         curNode =  self.head
#         while curNode:
#             yield curNode
#             curNode = curNode.next


# class Stack:
#     def __init__(self):
#         self.LinkedList = LinkedList()   

#     def __str__(self):
#         values = [str(x.data) for x in self.LinkedList]
#         return '\n'.join(values)      

#     def isEmpty(self):
#         if self.LinkedList.head is None:
#             return True
#         else:
#             return False
        
#     def push(self,data):
#         node = Node(data)
#         node.next = self.LinkedList.head
#         self.LinkedList.head = node

#     def pop(self):
#         if self.isEmpty:
#             return "Stack is Empty."
#         else:    
#             temp = self.LinkedList.head.data
#             self.LinkedList.head = self.LinkedList.head.next
#             return temp.data
    
# mystack = Stack()  
# mystack.push(34)  
# mystack.push(54)
# mystack.push(64)
# print(mystack.pop())  
# print(mystack)


class Node:
    def __init__(self,data = None):
        self.data = data
        self.next = None

    # def __setattr__(self, name, data):
    #     return str(self.data)    

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        curNode =  self.head
        while curNode:
            yield curNode
            curNode = curNode.next    

class Queue:
    def __init__(self):
        self.LinkedList = LinkedList()   

    def __str__(self):
        values = [str(x.data) for x in self.LinkedList]
        return '\n'.join(values)      

    def isEmpty(self):
        if self.LinkedList.head is None:
            return True
        else:
            return False
        
    def enqueue(self,data):
        node = Node(data)
        if self.LinkedList.head is None:
            self.LinkedList.head = node
            self.LinkedList.tail = node
        else:
            self.LinkedList.tail.next = node
            self.LinkedList.tail = node  

    def pop(self):
        if self.isEmpty():
            return "Queue is Empty."
        else:    
            temp = self.LinkedList.head.data
            self.LinkedList.head = self.LinkedList.head.next
            return temp   
    def peek(self):
        if self.isEmpty():
            return "There is not any node in the Queue"
        else:
            return self.LinkedList.head
    
myqueue = Queue()
myqueue.enqueue(1)
myqueue.enqueue(2)
myqueue.enqueue(3)
print(myqueue) 
myqueue.pop()
print(myqueue)
myqueue.peek()
