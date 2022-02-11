# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of DSA course available on CourseGalaxy.com  

def shell_sort(a):
    h = int(input("Enter maximum increment(odd value) : "))
    while h>=1:
        for i in range(h,len(a)):  
            temp = a[i]
            j=i-h
            while j >= 0 and a[j] > temp:
                a[j+h] = a[j]
                j=j-h
            a[j+h] = temp
        h=h-2

##############################################################

list1 = [65,73,21,90,6,239,3,35,1,15,5,9,8,23,12,5,7,2,19,34,]
shell_sort(list1)
print(list1)

