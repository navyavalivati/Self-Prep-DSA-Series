"""
Given an array (or string), the task is to reverse the array/string.
Examples : 
 

Input  : arr[] = {1, 2, 3}
Output : arr[] = {3, 2, 1}

Input :  arr[] = {4, 5, 1, 2}
Output : arr[] = {2, 1, 5, 4}

"""

#n=int(input())  #size of array
#a=list(map(int,input().split())) #array input

#reversing array can be done in many ways.

#using list slicing.
"""
res = a[::-1]
print(res)

"""
#using reverse method.

#a.reverse()
#print(a)

#using while loop
"""
j=len(a)-1
i=0
while(i<j):
    temp=a[i]
    a[i]=a[j]
    a[j]=temp
    i+=1
    j-=1

print(a)

"""
#Another Approach

def reverseArray(a,low,high):
    if(low>=high):
        return
    
    a[low],a[high]=a[high],a[low]
    reverseArray(a,low+1,high-1)


a = []
n=int(input())
for i in range(0,n):
    x=int(input())
    a.append(x)

reverseArray(a,0,n-1)
print(a)
