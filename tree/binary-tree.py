# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of DSA course available on CourseGalaxy.com  

from collections import deque

class Node:
    def __init__(self,value):
        self.info = value 
        self.lchild = None
        self.rchild = None

class BinaryTree:
    def __init__(self): 
        self.root = None
    
    def is_empty(self):
        return self.root == None
        
    def display(self):
        self._display(self.root,0)
        print()
        
    def _display(self,p,level):
        if p is None:
            return
        self._display(p.rchild, level+1)
        print()

        for i in range(level):
            print("    ", end='')
        print(p.info)
        self._display(p.lchild, level+1) 
        
    def preorder(self):
        self._preorder(self.root)
        print()
    
    def _preorder(self,p):
        if p is None:
            return
        print(p.info, " ", end ='')
        self._preorder(p.lchild)
        self._preorder(p.rchild) 
        
    def inorder(self):
        self._inorder(self.root)
        print()

    def _inorder(self, p):
        if p is None :
            return
        self._inorder(p.lchild)
        print(p.info, " ", end ='')
        self._inorder(p.rchild) 

    def postorder(self):
        self._postorder(self.root)
        print() 
         
    def _postorder(self, p):
        if p is None:
            return
        self._postorder(p.lchild)
        self._postorder(p.rchild) 
        print(p.info, " ", end ='') 

    def level_order(self):
        if self.root is None:
            print("Tree is empty")
            return
              	     
        qu = deque()
        qu.append(self.root)

        while len(qu)!=0:
            p = qu.popleft()
            print(p.info + " ",end='')
            if p.lchild is not None:
                qu.append(p.lchild)
            if p.rchild is not None:
                qu.append(p.rchild)
    	     
    
    def height(self):
        return self._height(self.root) 

    def _height(self,p):
        if p is None:
            return 0 

        hL = self._height(p.lchild) 
        hR = self._height(p.rchild) 

        if hL > hR:
            return 1 + hL 
        else:
            return 1 + hR

    def create_tree(self):
        self.root = Node('P') 
        self.root.lchild = Node('Q') 
        self.root.rchild = Node('R') 
        self.root.lchild.lchild = Node('A') 
        self.root.lchild.rchild = Node('B') 
        self.root.rchild.lchild = Node('X') 
     
        
#################################################################            
bt = BinaryTree()

bt.create_tree() 

bt.display() 
print() 

print("Preorder : ") 
bt.preorder()  
print("") 

print("Inorder : ") 
bt.inorder() 
print() 

print("Postorder : ") 
bt.postorder() 
print() 

print("Level order : ") 
bt.level_order() 
print() 

print("Height of tree is " , bt.height())

