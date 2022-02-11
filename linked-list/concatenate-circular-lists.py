# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of DSA course available on CourseGalaxy.com  

class Node(object):

    def __init__(self,value):
        self.info = value 
        self.link = None
        

class CircularLinkedList(object):

    def __init__(self):
        self.last = None

    def display_list(self):
        if self.last == None:
            print("List is empty\n")
            return

        p = self.last.link

        while True:
            print(p.info , " ",end='')
            p = p.link
            if  p == self.last.link:
                break
        print() 

    def insert_in_empty_list(self,data):
        temp = Node(data) 
        self.last = temp 
        self.last.link = self.last 
      

    def insert_at_end(self,data):
        temp = Node(data) 
        temp.link = self.last.link 
        self.last.link = temp 
        self.last = temp 
      

    def create_list(self):
        n = int(input("Enter the number of nodes : "))
        if n == 0:
            return
        data = int(input("Enter the element to be inserted : "))
        self.insert_in_empty_list(data)
        
        # for(i = 2  i <= n  i++)
        for i in range(n-1):
            data = int(input("Enter the element to be inserted : "))
            self.insert_at_end(data)
            
    def concatenate(self,list2):
        if self.last is None:
            self.last = list.last;
            return

        if list2.last is None:
            return

        p = self.last.link;
        self.last.link = list2.last.link;
        list2.last.link = p;
        self.last = list2.last;
        
 
###############################################################
list1 = CircularLinkedList()
list2 = CircularLinkedList()

print("Enter first list :- ")
list1.create_list()

print("Enter second list :- ")
list2.create_list()

print("First ");   list1.display_list()
print("Second ");  list2.display_list()

list1.concatenate(list2)
print("First ")
list1.display_list()


                
