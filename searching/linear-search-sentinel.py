# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of DSA course available on CourseGalaxy.com  

def Search(a, n, searchValue):
    a[n] = searchValue
    i = 0
    while searchValue != a[i]:
        i+=1
    if i < n:
        return i
    else:
        return -1


n = int(input("Enter the number of elements : "))
a = [None]*(n+1)
print("Enter the elements - ")
for i in range(n):
    a[i] = int(input("Enter element : "))  

searchValue = int(input("Enter the search value : "))
index = Search(a, n, searchValue)

if index == -1:
    print("Value ", searchValue ," not present in the list")
else:
    print("Value ", searchValue ," present at index " , index)

    


