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
        p = self.start
        while p is not None:
            if p.info == x:
                break
            p = p.link

        if p is None:
            print(x, "not present in the list")
        else:
            temp = Node(data)
            temp.link = p.link
            p.link = temp
            
     
            
    def insert_before(self, data, x):
        # If list is empty
        if self.start is None:
            print("List is empty") 
            return 
    
        # x is in first node,new node is to be inserted before first node
        if x == self.start.info:
            temp = Node(data) 
            temp.link = self.start 
            self.start = temp 
            return 
        
        # Find reference to predecessor of node containing x
        p = self.start 
        while p.link is not None: 
            if p.link.info == x:
                break 	
            p = p.link 


        if p.link is None:
             print(x , " not present in the list") 
        else:
            temp = Node(data) 
            temp.link = p.link 
            p.link = temp
    
     

    def insert_at_position(self, data, k):
        if k == 1:
            temp = Node(data) 
            temp.link = self.start  
            self.start = temp 
            return 
                    
        p = self.start
        i = 1
        while i<k-1 and p is not None: # find a reference to k-1 node
            p = p.link
            i+=1

        if p is None:
            print("You can insert only upto position",i) 
        else:
            temp = Node(data) 
            temp.link = p.link
            p.link = temp 

    def delete_node(self,x):
      
            if self.start is None:
                print("List is empty") 
                return 

            # Deletion of first node
            if self.start.info == x:
                self.start = self.start.link   
                return 

            # Deletion in between or at the end
            p = self.start 
            while p.link is not None:
                if p.link.info == x:
                    break 	
                p = p.link 

            if p.link is None:
                print("Element ", x ,"not in list") 
            else:
                p.link = p.link.link 
       
                 
    def delete_first_node(self):
      
        if self.start is None:
            return 
        self.start = self.start.link 
       

    def delete_last_node(self):
      
        if self.start is None:
            return 

        if self.start.link is None:
            self.start = None 
            return 
           
        p = self.start 
        while p.link.link is not None:
            p = p.link 
        p.link = None 

    def reverse_list(self):
      
        prev = None 
        p = self.start 
        while p is not None:
            next = p.link 
            p.link = prev 
            prev = p 
            p = next 
           
        self.start = prev 
           


    def bubble_sort_exdata(self):
        end=None

        while end != self.start.link:

            p = self.start
            while  p.link != end:
                q = p.link 
                if p.info > q.info:
                    p.info,q.info = q.info,p.info 
                p = p.link     
            end = p  

    
    def bubble_sort_exlinks(self):
        end = None  
        while end != self.start.link:
            r = p = self.start
            while p.link != end:
                q = p.link 
                if p.info > q.info :
                    p.link = q.link 
                    q.link = p 
                    if p!=self.start:
                        r.link = q 
                    else:
                        self.start = q 
                    p,q = q,p 
                r = p
                p = p.link
            end = p
   
           
    def has_cycle(self):
      
        if self.find_cycle() is None:
            return False 
        else:
            return True 
       

    def find_cycle(self):

        if self.start is None or self.start.link is None:
            return None 

        slowR = self.start
        fastR = self.start 

        while fastR is not None and fastR.link is not None:
            slowR = slowR.link 
            fastR = fastR.link.link 
            if slowR == fastR:
                return slowR 
        return None 


    def remove_cycle(self):
          
        c = self.find_cycle() 
        if c is None:
            return
        print("Node at which the cycle was detected is " , c.info) 
        
        p = c
        q = c 	
        lenCycle = 0 

        while True:
            lenCycle+=1
            q = q.link 
            if p == q:
                break;

        print("Length of cycle is :", lenCycle) 

        lenRemList = 0 
        p = self.start 
        while p != q:
            lenRemList+=1
            p = p.link 
            q = q.link
        
        print("Number of nodes not included in the cycle are : ", lenRemList) 

        length_list = lenCycle + lenRemList
        print("Length of the list is : " , length_list) 

        p = self.start 
        for i in range(length_list-1):
                p = p.link 
        p.link = None 
           

    def insert_cycle(self,x):
        if self.start is None:
            return
        p = self.start
        px = None
        prev = None 		

        while p is not None:
            if p.info == x:
                px = p
            prev = p
            p = p.link
                           
        if px is not None:
            prev.link = px 
        else:
            print(x , " not present in list")

    
    def merge2(self,list2):
        merge_list = SingleLinkedList()
        merge_list.start = self._merge2(self.start, list2.start)
        return merge_list
        
    def _merge2(self, p1, p2):

        if p1.info <= p2.info:
            startM = p1
            p1 = p1.link
        else:
            startM = p2
            p2 = p2.link
            
        pM = startM

        while p1 is not None and p2 is not None:
            if p1.info <= p2.info :
                pM.link = p1
                pM = pM.link
                p1 = p1.link
            else:
                pM.link = p2
                pM = pM.link
                p2 = p2.link
            
        if p1 is None:
            pM.link = p2
        else:
            pM.link = p1

        return startM
        


    def merge_sort(self):
        self.start = self._merge_sort_rec(self.start)
        

    def _merge_sort_rec(self,list_start):

        #if list empty or has one element
        if list_start is None or list_start.link is None: 
                return list_start

        #if more than one element
        start1 = list_start
        start2 = self._divide_list(list_start)
        start1 = self._merge_sort_rec(start1)
        start2 = self._merge_sort_rec(start2)
        startM = self._merge2(start1, start2)
        return startM
        

    def _divide_list(self, p):
        q = p.link.link
        while q is not None and q.link is not None:
            p = p.link
            q = q.link.link
        start2 = p.link
        p.link = None
        return start2
        
        

########################################################################################
            
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

   
