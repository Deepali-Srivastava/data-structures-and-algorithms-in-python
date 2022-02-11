# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of DSA course available on CourseGalaxy.com  

def heap_sort(a, n):
    build_heap_bottom_up(a, n)

    while n > 1:
        maxValue = a[1]
        a[1] = a[n]
        a[n] = maxValue
        n=n-1
        retsore_down(1, a, n)
        
def build_heap_bottom_up(a, n):
    i=n//2
    while i>=1:
        retsore_down(i, a, n)
        i=i-1

def retsore_down(i, a, n):
    k = a[i]
    lchild = 2 * i
    rchild = lchild + 1

    while rchild <= n:
        if k >= a[lchild] and k >= a[rchild]:
            a[i] = k
            return
        elif a[lchild] > a[rchild]:
            a[i] = a[lchild]
            i = lchild
        else:
            a[i] = a[rchild] 
            i = rchild 
                 
        lchild = 2 * i 
        rchild = lchild + 1 
             

    # If number of nodes is even
    if lchild == n and k < a[lchild]:
        a[i] = a[lchild] 
        i = lchild 
    a[i] = k 

###################################################
      
n = int(input("Enter the number of elements : "))
a = [None]*(n+1)
for i in range(1,n+1):
    a[i] = int(input("Enter element : "))

heap_sort(a,n)

for i in range(1,n+1):
    print(a[i], " ",end='') 
print()

###################################################

