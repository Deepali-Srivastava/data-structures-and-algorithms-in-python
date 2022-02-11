# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of DSA course available on CourseGalaxy.com  

class Node:
    def __init__(self,value):
        self.info = value 
        self.link = None 
   
def radix_sort(start):
    
    rear = [None] * 10 
    front = [None] * 10 

    leastSigPos = 1 
    mostSigPos = DigitsInLargest(start)

    for k in range(leastSigPos, mostSigPos+1):
        #Making all the queues empty at the beginning of each pass
        for i in range(10):
            rear[i] = None
            front[i] = None

        p = start
        while p is not None:
            #Find kth digit from right in the number
            dig = Digit(p.info, k)

            #Insert the node in Queue(dig)
            if front[dig] is None:
                front[dig] = p
            else:
                rear[dig].link = p
            rear[dig] = p

            p=p.link
               
        #Join all queues to form new linked list
        i = 0 
        while front[i] is None:  #Finding first non empty queue
            i=i+1

        start = front[i] 
        while i <= 8:
            if rear[i+1] is not None:   #if (i+1)th  queue is not empty
                rear[i].link = front[i+1] #join end of ith queue to start of (i+1)th queue
            else:
                rear[i+1] = rear[i]  #continue with rear[i]
            i=i+1 
        rear[9].link = None
    return start 

#Returns number of digits in the largest element of the list
def DigitsInLargest(start):
    #Find largest element
    large = 0
    p = start
    while p is not None:
        if p.info > large:
            large = p.info
        p = p.link
        
    #Find number of digits in largest element
    ndigits = 0
    while large != 0:
        ndigits = ndigits+1
        large//=10
    return ndigits 
   
#Returns kth digit from right in n
def Digit(n, k):
    d = 0 
    for i in range(1,k+1):
        d = n%10 
        n//=10 
    return d 
        

#################################################
start = None

n = int(input("Enter the number of elements : "))

for i in range(n):  #Inserting elements in linked list
    data = int(input("Enter element : "))

    temp = Node(data)
    if start is None:
        start = temp
    else:
        p = start
        while p.link is not None:
            p = p.link
        p.link = temp
            
start = radix_sort(start)

print("Sorted list is : ") 
p = start 
while p is not None :
    print(p.info , " ")
    p = p.link
print 

##################################################

