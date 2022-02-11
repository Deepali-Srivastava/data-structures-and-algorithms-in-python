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
        self.front = None
        self.rear = None
        self.size_queue = 0

    def is_empty(self):
        return self.front == None
    
    def size(self):
        return self.size_queue
    
    def enqueue(self, data):
        temp = Node(data)
        if self.front == None:
            self.front = temp
        else:
            self.rear.link = temp
        self.rear = temp
        self.size_queue+=1
                 
    def dequeue(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty")
        x = self.front.info
        self.front = self.front.link
        self.size_queue-=1
        return x

    def peek(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty")
        return self.front.info
        
    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        print("Queue is :   ")
        p = self.front 
        while p is not None:
            print(p.info, " ", end='')
            p = p.link 
        print()
    
    
#########################################################################################

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
        
