# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of DSA course available on CourseGalaxy.com  

def build_heap_top_down(a, n):
    for i in range(2, n+1):
        restore_up(i, a)

def build_heap_bottom_up(a, n):
    i=n//2
    while i>=1:
        restore_down(i, a, n)
        i=i-1
       
def restore_up(i, a):
    k = a[i]
    iparent = i // 2

    while a[iparent] < k :
        a[i] = a[iparent] 
        i = iparent 
        iparent = i // 2 
    a[i] = k

def restore_down(i, a, n):
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
     
####################################################
        
a1=[99999,20,33,15,6,40,60,45,16,75,10,80,12]
n1 = len(a1)-1

build_heap_bottom_up(a1,n1)

for i in range(1,n1+1):
    print(a1[i], " ",end='')
print()

a2=[99999,20,33,15,6,40,60,45,16,75,10,80,12]
n2 = len(a2)-1

build_heap_top_down(a2,n2) 

for i in range(1,n2+1):
    print(a2[i], " ",end='') 
print()

####################################################

         
     
 
