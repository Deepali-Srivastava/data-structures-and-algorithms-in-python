# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of DSA course available on CourseGalaxy.com  

class Node:

    def __init__(self,value):
        self.info = value 
        self.link = None 
        
class SingleLinkedList:

    def __init__(self):
        self.start = None
     
    def display_list(self):
        if self.start is None:
            print("List is empty")
            return
        else:
            print("List is :   ")
            p = self.start 
            while p is not None:
                print(p.info , " ", end='')
                p = p.link 
            print()

    def count_nodes(self):
        p = self.start 
        n = 0        
        while p is not None:
            n+=1
            p = p.link
        print("Number of nodes in the list = " ,n)
    
    def search(self,x):
        position = 1
        p = self.start
        while p is not None:
            if p.info == x:
                print(x , " is at position ", position)
                return True
            position+=1
            p = p.link
        else:
            print(x," not found in list")
            return False

    def insert_in_beginning(self, data):
        temp = Node(data)
        temp.link = self.start
        self.start = temp
   
    def insert_at_end(self, data):
        temp = Node(data)
        if self.start is None:
            self.start = temp
            return
        
        p = self.start
        while p.link is not None:
            p = p.link
        p.link = temp

    def create_list(self):
        n = int(input("Enter the number of nodes : "))
        if n == 0:
            return
        for i in range(n):
            data = int(input("Enter the element to be inserted : "))
            self.insert_at_end(data)
           
    def insert_after(self,data,x):
        pass    
           
    def insert_before(self, data, x):
        pass
     
    def insert_at_position(self, data, k):
        pass
    
    def delete_node(self,x):
        pass   
                 
    def delete_first_node(self):
        pass

    def delete_last_node(self):
        pass
    
    def reverse_list(self):
        pass   

    def bubble_sort_exdata(self):
        pass
    
    def bubble_sort_exlinks(self):
        pass
           
    def has_cycle(self):
        pass

    def find_cycle(self):
        pass

    def remove_cycle(self):
        pass   

    def insert_cycle(self,x):
        pass
    
    def merge2(self,list2):
        pass
    
    def _merge2(self, p1, p2):
        pass

    def merge_sort(self):
        pass    

    def _merge_sort_rec(self,listStart):
        pass

    def _divide_list(self, p):
        pass
        

#########################################################################################
            
list = SingleLinkedList() 

list.create_list() 
		
while True:
    print("1.Display list") 
    print("2.Count the number of nodes") 
    print("3.Search for an element")
    print("4.Insert in empty list/Insert in beginning of the list")
    print("5.Insert a node at the end of the list")
    print("6.Insert a node after a specified node")
    print("7.Insert a node before a specified node")
    print("8.Insert a node at a given position")
    print("9.Delete first node")
    print("10.Delete last node")
    print("11.Delete any node")
    print("12.Reverse the list")
    print("13.Bubble sort by exchanging data")
    print("14.Bubble sort by exchanging links")
    print("15.MergeSort")
    print("16.Insert Cycle")
    print("17.Detect Cycle")
    print("18.Remove cycle")
    print("19.Quit")
        
    option = int(input("Enter your choice : " ))

    if option == 1:
        list.display_list()
    elif option == 2:
        list.count_nodes()
    elif option == 3:
        data = int(input("Enter the element to be searched : "))
        list.search(data)
    elif option == 4:
        data = int(input("Enter the element to be inserted : "))
        list.insert_in_beginning(data)
    elif option == 5:
        data = int(input("Enter the element to be inserted : "))
        list.insert_at_end(data)
    elif option == 6:
        data = int(input("Enter the element to be inserted : "))
        x = int(input("Enter the element after which to insert : ")) 
        list.insert_after(data,x)
    elif option == 7:
        data = int(input("Enter the element to be inserted : "))
        x = int(input("Enter the element before which to insert : ")) 
        list.insert_before(data,x)
    elif option == 8:
        data = int(input("Enter the element to be inserted : "))
        k = int(input("Enter the position at which to insert : ")) 
        list.insert_at_position(data,k)
    elif option == 9:
        list.delete_first_node() 
    elif option == 10:
        list.delete_last_node() 
    elif option == 11:
        data = int(input("Enter the element to be deleted : ")) 
        list.delete_node(data)             
    elif option == 12:
        list.reverse_list()
    elif option == 13:
        list.bubble_sort_exdata() 
    elif option == 14:
        list.bubble_sort_exlinks() 
    elif option == 15:
        list.merge_sort() 
    elif option == 16:
        data = int(input("Enter the element at which the cycle has to be inserted : "))
        list.insert_cycle(data) 
    elif option == 17:
        if list.has_cycle():
            print("List has a cycle")
        else:
            print("List does not have a cycle") 
    elif option == 18:
        list.remove_cycle() 
    elif option == 19:
        break
    else:
        print("Wrong option") 
    print() 

   
