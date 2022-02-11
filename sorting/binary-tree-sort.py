# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of DSA course available on CourseGalaxy.com  

class Node:
    def __init__(self,value):
        self.info = value 
        self.lchild = None
        self.rchild = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def is_empty(self):
        return self.root == None
           
    def insert(self,x):
        self.root = self._insert(self.root, x)
                 
    def _insert(self,p, x):
        if p is None:
            p = Node(x)
        elif x < p.info :
            p.lchild = self._insert(p.lchild, x) 
        else:
            p.rchild = self._insert(p.rchild, x)   
        return p

    def inorder(self):
        self._inorder(self.root)
        print()

    def _inorder(self, p):
        if p is None :
            return
        self._inorder(p.lchild)
        print(p.info, " ")
        self._inorder(p.rchild) 

    
####################################
n = int(input("Enter the number of elements to be sorted : "))

tree = BinarySearchTree()          
for i in range(n):
    x = int(input("Enter element : "))
    tree.insert(x)
    
tree.inorder()  

####################################

