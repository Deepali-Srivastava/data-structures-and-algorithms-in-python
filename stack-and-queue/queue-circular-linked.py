# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of DSA course available on CourseGalaxy.com  

class EmptyQueueError(Exception):
    pass

class Node:

    def __init__(self,value):
        self.info = value 
        self.link = None 
        
class Queue:

    def __init__(self):
        self.rear = None
       
    def is_empty(self):
        return self.rear == None
            
    def size(self):
        if self.is_empty():
            return 0
        n = 0        
        p = self.rear.link
        while True:
            n+=1
            p = p.link
            if  p == self.rear.link:
                break
        return n
    
    def enqueue(self, data):
        temp = Node(data)
        
        if self.is_empty():
            self.rear = temp
            self.rear.link = self.rear
        else:
            temp.link = self.rear.link 
            self.rear.link = temp 
            self.rear = temp
        
    def dequeue(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is Empty")
        
        if self.rear.link == self.rear: #List has only one node
            temp = self.rear
            self.rear = None 
        else:
            temp = self.rear.link
            self.rear.link = self.rear.link.link 
        return temp.info

    def peek(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is Empty")
        return self.rear.link.info

    def display(self):
        if self.is_empty():
            print("List is empty")
            return

        p = self.rear.link
        while True:
            print(p.info , " ",end='')
            p = p.link
            if p == self.rear.link:
                break
        print()
        
########################################################################

if __name__ == "__main__":
    qu = Queue()

    while True:
        print("1.Enqueue") 
        print("2.Dequeue")
        print("3.Peek")
        print("4.Size") 
        print("5.Display")  
        print("6.Quit") 
         
        choice = int(input("Enter your choice : "))

        if choice == 1:
            x=int(input("Enter the element : "))
            qu.enqueue(x) 
        elif choice == 2:
            x=qu.dequeue() 
            print("Element deleted from the queue is : " , x) 
        elif choice == 3:
            print("Element at the front end is " , qu.peek()) 
        elif choice == 4:
            print("Size of queue ", qu.size()) 
        elif choice == 5:
            qu.display() 
        elif choice == 6:
          break;
        else:
          print("Wrong choice") 
        print()

