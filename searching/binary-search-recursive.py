# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of DSA course available on CourseGalaxy.com  

def binary_search(a, n, searchValue):
    return _search(a, 0, n-1, searchValue)

def _search(a, first, last, searchValue):
    if (first > last):
        return -1
    mid = (first + last) // 2
    if searchValue > a[mid]:	 #Search in right half
        return _search(a, mid+1, last, searchValue)
    elif searchValue < a[mid]:	 #Search in left half
        return _search(a, first, mid-1, searchValue)
    else:
        return mid
    
############################################################
    
n = int(input("Enter the number of elements : "))
a = [None]*n
print("Enter the elements in sorted order  - ")
for i in range(n):
    a[i] = int(input("Enter element : "))  

searchValue = int(input("Enter the search value : "))
index = binary_search(a, n, searchValue)

if index == -1:
    print("Value " , searchValue , " not present in the array")
else:
    print("Value " , searchValue , " present at index " , index)
