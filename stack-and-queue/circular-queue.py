# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of DSA course available on CourseGalaxy.com  

class EmptyQueueError(Exception):
    pass

class Queue:
    
    def __init__(self,default_size=10):
        self.items = [None] * default_size
        self.front = 0
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def size(self):
        return self.count
    
    def enqueue(self, item):
        if self.count == len(self.items):
            self.resize( 2*len(self.items) )
            
        i = (self.front + self.count) % len(self.items)
        self.items[i] = item
        self.count+=1
        
    def dequeue(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty")

        x = self.items[self.front]
        self.items[self.front] = None
        self.front = (self.front + 1) % len(self.items)
        self.count-=1
        return x

    def peek(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty")
        return self.items[self.front]
        
    def display(self):
        print(self.items)
        
    def resize(self,newsize):
        old_list = self.items
        self.items = [None]*newsize
        i = self.front
        for j in range(self.count):
            self.items[j] = old_list[i]
            i = (1+i)%len(old_list)
        self.front = 0 

###########################################################

if __name__ == "__main__":
    qu = Queue(6)

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
          break
        else:
          print("Wrong choice") 
        print()
