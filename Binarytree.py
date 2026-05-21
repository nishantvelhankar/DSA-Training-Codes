# types of binary tree
#1.full binary tree
# -> i)each node has either 0 or 2 child
#   ii) No node has single child

# 2. complete binary tree
# -> i) all levels except possibly the last are completely filled
#    ii) Nodes in the last level are filled from left to right

# 3. perfect binary tree
# -> i) all internal nodes have exactly two nodes
#    ii) all leaf nodes are at the same level



# pre order(Root Left Right)
# n1-n2-n4-n9-n10-n5-n3-n6-n7

# inorder(left root right)

# post order(Left right root)

# binary search tree
# -> it performs faster than binary tree when inserting and deleting nodes


# pre order -> 70-50-30-20-10-40-60-90-80-100
# inorder ->  
# postorder ->

# class BSTNode:
#     def __init__(self, data):
#         self.data = data
#         self.leftchild = None
#         self.rightchild = None


# def insertNode(rootnode, nodevalue):
#     if rootnode.data == None:
#         rootnode.data = nodevalue

#     elif nodevalue <= rootnode.data:
#         if rootnode.leftchild is None:
#             rootnode.leftchild = BSTNode(nodevalue)
#         else:
#             insertNode(rootnode.leftchild, nodevalue)

#     else:
#         if rootnode.rightchild is None:
#             rootnode.rightchild = BSTNode(nodevalue)
#         else:
#             insertNode(rootnode.rightchild, nodevalue)


# def preOrderTraversal(rootnode):
#     if not rootnode:
#         return
#     print(rootnode.data,end=' ')
#     preOrderTraversal(rootnode.leftchild)
#     preOrderTraversal(rootnode.rightchild)

# def inOrderTraversal(rootnode):
#     if not rootnode:
#         return
#     inOrderTraversal(rootnode.leftchild)
#     print(rootnode.data,end=' ')
#     inOrderTraversal(rootnode.rightchild)

# def postOrderTraversal(rootnode):
#     if not rootnode:
#         return
#     postOrderTraversal(rootnode.leftchild)
#     postOrderTraversal(rootnode.rightchild)
#     print(rootnode.data,end=' ')

# def searchNode(rootnode, nodevalue):
#     if rootnode.data == nodevalue:
#         print("The value is Root Node")

#     elif nodevalue < rootnode.data:
#         if rootnode.leftchild is None:
#             print("Value not found")
#         elif rootnode.leftchild.data == nodevalue:
#             print(f"{nodevalue} is on the LEFT side of {rootnode.data}")
#         else:
#             searchNode(rootnode.leftchild, nodevalue)

#     else:
#         if rootnode.rightchild is None:
#             print("Value not found")
#         elif rootnode.rightchild.data == nodevalue:
#             print(f"{nodevalue} is on the RIGHT side of {rootnode.data}")
#         else:
#             searchNode(rootnode.rightchild, nodevalue)

# newBST = BSTNode(70)

# insertNode(newBST, 50)
# insertNode(newBST, 90)
# insertNode(newBST, 30)
# insertNode(newBST, 60)
# insertNode(newBST, 80)
# insertNode(newBST, 100)
# insertNode(newBST, 20)
# insertNode(newBST, 40)
# insertNode(newBST, 95)
# insertNode(newBST, 10)

# # print()
# # print('Preorder')
# # preOrderTraversal(newBST)
# # print('\n')
# # print('Inorder')
# # inOrderTraversal(newBST)
# # print('\n')
# # print('Postorder')
# # postOrderTraversal(newBST)
# # print('\n')
# # searchNode(newBST,20)

# while True:
#     print()
#     print("==================")
#     print("1. Insert node")
#     print("2. PreOrder Traversal")
#     print("3. InOrder Traversal")
#     print("4. PostOrder Traversal")
#     print("5. Search Node")
#     print("6. EXIT")
#     print("==================")

#     choice = int(input("Enter your Choice: "))
#     if choice == 1:
#         nodevalue = int(input("Enter Node to add: "))
#         insertNode(newBST, nodevalue)
#     elif choice == 2:
#         preOrderTraversal(newBST)
#     elif choice == 3:
#         inOrderTraversal(newBST)
#     elif choice == 4:
#         postOrderTraversal(newBST)
#     elif choice == 5:
#         nodevalue=int(input('Enter node to find:'))
#         searchNode(newBST,nodevalue)
#     else:
#         sys.exit()



