# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of DSA course available on CourseGalaxy.com  

class Node(object):

    def __init__(self,value):
        self.info = value 
        self.link = None 
        
class SortedLinkedList(object):

    def __init__(self):
        self.start = None

    def insert_in_order(self, data):
            temp = Node(data) 

            # List empty or node to be inserted before first node 
            if self.start == None or data < self.start.info:
                temp.link = self.start 
                self.start = temp 
                return 

            p = self.start 
            while p.link is not None and p.link.info <= data:
                p = p.link
            temp.link = p.link 
            p.link = temp 
          

    def create_list(self):
        n = int(input("Enter the number of nodes : "))
        if n == 0:
            return
        
	for i in range(n):
            data = int(input("Enter the element to be inserted : "))
            self.insert_in_order(data)
        
    def search(self, x):
        if self.start is None:
            print("List is empty")
            return
        p = self.start
        position = 1
        while  p is not None and p.info <= x:
            if  p.info == x:
                break
            position+=1
            p = p.link

        if p is None or p.info != x:
            print(x," not found in list")
        else:
            print(x , " is at position " , position) 	
          
    def display_list(self):
        if self.start is None:
            print("List is empty")
            return
        print("List is :   ")
        p = self.start
        while p is not None:
            print(p.info , "  ", end='')
            p = p.link
        print()
        
#########################################################################
        
list = SortedLinkedList() 
list.create_list() 
		
while True:
    print("1.Display list") 
    print("2.Insert")
    print("3.Search for an element")
    print("4.Quit")
        
    option = int(input("Enter your choice : " ))

    if option == 1:
        list.display_list()
    elif option == 2:
        data = int(input("Enter the element to be inserted : "))
        list.insert_in_order(data)
    elif option == 3:
        data = int(input("Enter the element to be searched : "))
        list.search(data)
    elif option == 4:
        break
    else:
        print("Wrong option") 
    print() 

   
       

