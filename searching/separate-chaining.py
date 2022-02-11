# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of DSA course available on CourseGalaxy.com  

##################################################################

class studentRecord:
    def __init__(self,i,name):
        self.studentId = i
        self.studentName = name

    def get_student_id(self):
        return self.studentId

    def set_student_id(self,i):
        self.studentId = i
        
    def __str__(self):
        return str(self.studentId) + " "  + self.studentName 

##################################################################
    
class Node:
    def __init__(self,value):
        self.info = value 
        self.link = None 
        
##################################################################

class SingleLinkedList:
    def __init__(self):
        self.start = None

    def display_list(self):
        if self.start is None:
            print("___")
            return
        p = self.start 
        while p is not None:
            print(p.info , " ", end='')
            p = p.link 
        print()
    
    def search(self,x):
        p = self.start
        while p is not None:
            if p.info.get_student_id() == x:
                return p.info
            p = p.link
        else:
            return None

    def insert_in_beginning(self, data):
        temp = Node(data)
        temp.link = self.start
        self.start = temp
    
    def delete_node(self,x):
        if self.start is None:
            print("List is empty") 
            return 

        # Deletion of first node
        if self.start.info.get_student_id() == x:
            self.start = self.start.link   
            return 

        # Deletion in between or at the end
        p = self.start 
        while p.link is not None:
            if p.link.info.get_student_id() == x:
                break 	
            p = p.link 

        if p.link is None:
            print("Element ", x ,"not in list") 
        else:
            p.link = p.link.link
            
##################################################################
   

class HashTable:

    def __init__(self,tableSize):
        self.m = tableSize   
        self.array = [None] * self.m
        self.n = 0  

    def hash(self, key):
        return (key % self.m)

    def display_table(self):
        for i in range(self.m):
            print( "[" , i , "]  -->  ", end ='' )
            if self.array[i]!= None:
                self.array[i].display_list()
            else:
               print("___")
        
    
    def search(self, key):
        h = self.hash(key)
        if self.array[h] != None:
            return self.array[h].search(key)
        return None        
               
    def insert(self, newRecord):
        key = newRecord.get_student_id()
        h = self.hash(key)

        if self.array[h] == None:
            self.array[h] = SingleLinkedList()
        self.array[h].insert_in_beginning(newRecord)
        self.n+=1
    
   
   
    def delete(self, key):
        h = self.hash(key)
        if self.array[h] != None:
            self.array[h].delete_node(key)
            self.n-=1
        else:
            print("Value " , key , " not present")

    
                
##################################################################
               
size = int(input("Enter size of table : "))
table = HashTable(size)

while True:
    print("1.Insert a record")
    print("2.Search a record")
    print("3.Delete a record")
    print("4.Display table")
    print("5.Exit")

    choice = int(input("Enter your choice : "))
    if choice == 1:
        id = int(input("Enter student id : "))
        name = input("Enter student name : ")
        aRecord = studentRecord(id,name)
        table.insert(aRecord)
    elif choice == 2:
        id = int(input("Enter a key to be searched : "))
        aRecord = table.search(id)
        if  aRecord is None:
            print("Key not found")
        else:
            print(aRecord)
    elif choice == 3:
          id = int(input("Enter a key to be deleted :"))
          table.delete(id)
    elif choice == 4:
          table.display_table()
    elif choice == 5:
          break
    else:
          print("Wrong option") 
    print() 

        

                        
