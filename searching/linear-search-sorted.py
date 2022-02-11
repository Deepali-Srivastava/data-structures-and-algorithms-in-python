# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of DSA course available on CourseGalaxy.com  

def Search(a, n, searchValue):
    for i in range(n):
        if a[i] >= searchValue:
            break
        
    if a[i] ==  searchValue:
        return i
    else:
        return -1
            
###########################################################

n = int(input("Enter the number of elements : "))
a = [None]*n
print("Enter the elements in sorted order  - ")
for i in range(n):
    a[i] = int(input("Enter element : "))  

searchValue = int(input("Enter the search value : "))
index = Search(a, n, searchValue)

if index == -1:
    print("Value " , searchValue , " not present in the list")
else:
    print("Value " , searchValue , " present at index " , index)

    


