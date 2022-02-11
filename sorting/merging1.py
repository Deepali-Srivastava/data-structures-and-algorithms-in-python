# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of DSA course available on CourseGalaxy.com  

#a[low1]...a[up1] and a[low2]...a[up2] merged to temp[low1]..temp[up2]
def merge(a,temp,low1,up1,low2,up2):
      i = low1
      j = low2
      k = low1
           
      while i <= up1 and j <= up2:
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

###########################################

a = [1,2,4,6,  3,5,6,7,13,19]

temp=[None]*len(a)

merge(a,temp,0,3,4,9)

print("Merged list temp is : ");
print(temp)            


##########################################
