# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of DSA course available on CourseGalaxy.com  

def insertion_sort(a):
    for i in range(1,len(a)):  
        temp = a[i]
        j = i-1
        while j >= 0 and a[j] > temp:
            a[j+1] = a[j]
            j=j-1
        a[j+1] = temp
            
####################################

list1 = [6,3,1,5,9,8]
insertion_sort(list1)
print(list1)

list2 = [2,3,5,39,11,8,9,166,45,23]
insertion_sort(list2)
print(list2)

list3 = [1,2,3,4,5,6,7,8,9,10]
insertion_sort(list3)
print(list3)

list4 = [10,9,8,7,6,5,4,3,2,1]
insertion_sort(list4)
print(list4)

list5 = [4]
insertion_sort(list5)
print(list5)

#####################################
