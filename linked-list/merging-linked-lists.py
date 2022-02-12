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
    

    def bubble_sort_exdata(self):
        end = None
        while end != self.start.link:

            p = self.start
            while  p.link != end:
                q = p.link 
                if p.info > q.info:
                    p.info,q.info = q.info,p.info 
                p = p.link     
            end = p

    def merge1(self, list2):
        merge_list = SingleLinkedList()
        merge_list.start = self._merge1(self.start, list2.start)
        return merge_list
    
    def _merge1(self, p1, p2):
        if p1.info <= p2.info:
            startM = Node(p1.info)
            p1 = p1.link
        else:
            startM = Node(p2.info)
            p2 = p2.link;
        
        pM = startM

        while p1 is not None and p2 is not None:
            if p1.info <= p2.info :
                pM.link = Node(p1.info)
                p1 = p1.link
            else:
                pM.link = Node(p2.info);
                p2 = p2.link;
            pM = pM.link;
            

        #If second list has finished and elements left in first list
        while p1 is not None:
            pM.link = Node(p1.info)
            p1 = p1.link
            pM = pM.link
        
        #If first list has finished and elements left in second list
        while p2 is not None:
            pM.link = Node(p2.info)
            p2 = p2.link
            pM = pM.link

        return startM

        
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
        

#########################################################################################

list1 = SingleLinkedList()
list2 = SingleLinkedList()

list1.create_list() 
list2.create_list()

list1.bubble_sort_exdata()
list2.bubble_sort_exdata()
	
print("First List - "); list1.display_list()
print("Second List - "); list2.display_list()

list3 = list1.merge1(list2)
print("Merged List - "); list3.display_list()
		
print("First List - "); list1.display_list()
print("Second List - "); list2.display_list()
		
list3 = list1.merge2(list2)
print("Merged List - "); list3.display_list()
print("First List - ");  list1.display_list()
print("Second List - "); list2.display_list()

