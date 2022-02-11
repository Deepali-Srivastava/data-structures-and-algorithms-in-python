# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of DSA course available on CourseGalaxy.com  

def merge_sort(a):
    n=len(a)
    temp = [None]*n
    size = 1
    while size <= n-1:
        sort_pass(a, temp, size, n)
        size = size * 2 
             
def sort_pass(a,temp,size,n):
    low1 = 0
    while low1+size <= n-1:
        up1 = low1 + size - 1
        low2 = low1 + size
        up2 = low2 + size - 1

        if up2 >= n: # if length of last sublist is less than size
            up2 = n-1
            
        merge(a, temp, low1, up1, low2, up2)

        low1 = up2 + 1  # Take next two sublists for merging
        
    for i in range(low1,n):
        temp[i] = a[i]  # If any sublist is left alone
        
    copy(a, temp, n)  

# a[low1]...a[up1] and a[low2]...a[up2] merged to temp[low1]...temp[up2] */
def merge(a, temp, low1, up1, low2, up2):
    i = low1 
    j = low2 
    k = low1 

    while i <= up1  and j <= up2:
            if a[i] <= a[j]:
                temp[k] = a[i]
                i+=1
            else:
                temp[k] = a[j]
                j+=1
            k+=1
    
    while i <= up1:
                temp[k] = a[i]
                i+=1
                k+=1
            
    while j <= up2:
                temp[k] = a[j]
                j+=1
                k+=1

# copies temp[low]....temp[up] to a[low]...a[up]
def copy(a, temp, n):
    for i in range(n):
        a[i] = temp[i] 


#############################################################    
             
list1 = [6,3,1,5,9,8]
merge_sort(list1)
print(list1)

list2 = [2,3,5,39,11,8,9,166,45,23]
merge_sort(list2)
print(list2)

list3 = [1,2,3,4,5,6,7,8,9,10]
merge_sort(list3)
print(list3)

list4 = [10,9,8,7,6,5,4,3,2,1]
merge_sort(list4)
print(list4)

list5 = [4]
merge_sort(list5)
print(list5)

#################################################################
