# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of DSA course available on CourseGalaxy.com  

def binary_search(a, n, searchValue):
    first = 0
    last = n-1

    while first <= last :
        mid = (first + last)//2 
        if searchValue < a[mid]:
            last = mid-1     # Search in left half 
        elif searchValue > a[mid]:
            first = mid+1    # Search in right half
        else:
            return mid	     # searchValue present at index mid
    return -1

####################################################

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


