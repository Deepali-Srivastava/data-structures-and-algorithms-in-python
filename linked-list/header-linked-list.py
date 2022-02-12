# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of DSA course available on CourseGalaxy.com  

class Node(object):

    def __init__(self,value):
        self.info = value 
        self.link = None 

class HeaderLinkedList(object):

    def __init__(self):
        self.head = Node(0)

    def display_list(self):
        if self.head.link == None:
            print("List is empty")
            return

        p = self.head.link
        print("List is : ")
        while p is not None:
            print(p.info, " ", end='')
            p = p.link
        print() 
	     
       

    def create_list(self):
        n = int(input("Enter the number of nodes : "))
        for i in range(n):
            data = int(input("Enter the element to be inserted : "))
            self.insert_at_end(data)


    def insert_at_end(self,data):
            
        temp = Node(data) 

        p = self.head 
        while p.link is not None:
            p = p.link 

        p.link = temp 
        temp.link = None
        
    def insert_before(self, data, x):
        # Find pointer to predecessor of node containing x
        p = self.head
        while  p.link is not None:
            if p.link.info == x:
                break
            p = p.link
            
        if p.link is None:
            print(x , " not present in the list")
        else:
            temp = Node(data)
            temp.link = p.link
            p.link = temp
 
    def insert_at_position(self,data,k):
        p = self.head
        i = 1
        while i <= k-1 and p is not None:
            p = p.link
            i+=1
            
        if p is None:
            print("You can insert only upto " , (i-1) , "th position ")
        else:
            temp = Node(data)
            temp.link = p.link
            p.link = temp 
    
    def delete_node(self,data):
        p = self.head
        while p.link is not None:
            if p.link.info == data:
                break
            p = p.link
        
        if p.link == None:
            print(data + "Element %d not found")
        else:
            p.link = p.link.link 
         
    def reverse_list(self):
        prev = None 
        p = self.head.link 
        while p is not None:
            next = p.link 
            p.link = prev 
            prev = p 
            p = next 

        self.head.link = prev 
            
list = HeaderLinkedList()

list.create_list() 
		
while True:
    print("1.Display list") 
    print("2.Insert a node at the end of the list")
    print("3.Insert a node before a specified node")
    print("4.Insert a node at a given position")
    print("5.Delete a node")
    print("6.Reverse the list")
    print("7.Quit")
        
    option = int(input("Enter your choice : " ))

    if option == 1:
        list.display_list()
    elif option == 2:
        data = int(input("Enter the element to be inserted : "))
        list.insert_at_end(data)
    elif option == 3:
        data = int(input("Enter the element to be inserted : "))
        x = int(input("Enter the element before which to insert : ")) 
        list.insert_before(data,x)
    elif option == 4:
        data = int(input("Enter the element to be inserted : "))
        k = int(input("Enter the position at which to insert : ")) 
        list.insert_at_position(data,k)
    elif option == 5:
        data = int(input("Enter the element to be deleted : ")) 
        list.delete_node(data)             
    elif option == 6:
        list.reverse_list()
    elif option == 7:
        break
    else:
        print("Wrong option") 
    print() 
