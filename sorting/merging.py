# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of DSA course available on CourseGalaxy.com  

def merge(a1,a2,temp):
      i = 0
      j = 0
      k = 0
      n1=len(a1)
      n2=len(a2)
      
      while i <= n1-1 and j <= n2-1:
          if a1[i] < a2[j]:
              temp[k] = a1[i]
              i+=1
          else:
              temp[k] = a2[j]
              j+=1
          k+=1
        
      # copy remaining elements of a1, list a2 finished
      while i <= n1-1:
          temp[k] = a1[i]
          i+=1
          k+=1
            
      # copy remaining elements of a2, list a1 finished
      while j <= n2-1:
          temp[k] = a2[j]
          j+=1
          k+=1

          
#####################################################################
n1 = int(input("Enter the number of elements in list a1 : "))
print("Enter elements in sorted order : " );
a1 = [None]*n1
for i in range(n1):
    a1[i] = int(input("Enter element : "))

n2 = int(input("Enter the number of elements in list a2 : "))
print("Enter elements in sorted order : " );
a2 = [None]*n2
for i in range(n2):
    a2[i] = int(input("Enter element : "))

temp=[None]*(n1+n2)

merge(a1,a2,temp)

print("Merged list temp is : ");
print(temp)            

#####################################################################
