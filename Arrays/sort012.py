"""
Given an array A[] consisting 0s, 1s and 2s. The task is to write a function that sorts the given array. The functions should put all 0s first, then all 1s and all 2s in last.
Examples: 
 

Input: {0, 1, 2, 0, 1, 2}
Output: {0, 0, 1, 1, 2, 2}

Input: {0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1}
Output: {0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2}

"""
#using sort in built function.
"""
a=[]
n=int(input())
for i in range(0,n):
    x=int(input())
    a.append(x)

a.sort(reverse=False)
for i in range(0,n):
    print(a[i],end=" ")

print()

TC: O(NlogN)
SC: O(1)
"""
#Another approach is to count number of 0's, no. of 1's and no. of 2's separately 
#after counting, put all 0's first, then 1's and then 2's in array.
"""
This solution may not work if values are a part of the structure.
For example, consider a situation where 0 represents Computer Science Stream, 1 represents Electronics and 2 represents Mechanical.
We have a list of student objects (or structures) 
and we want to sort them. We cannot use the above sort as we simply put 0s, 1s, and 2s one by one.


def sort012(a,n):
    c0=0
    c1=0
    c2=0
    for i in range(0,n):
        if(a[i]==0):
            c0+=1
        if(a[i]==1):
            c1+=1
        if(a[i]==2):
            c2+=1

    for i in range(0,c0):
        a[i]=0
    for i in range(c0,(c0+c1)):
        a[i]=1
    for i in range((c0+c1),n):
        a[i]=2

    return

a=[]
n=int(input())
for i in range(0,n):
    x=int(input())
    a.append(x)

sort012(a,n)
for i in range(0,n):
    print(a[i],end=" ")

print()

TC: O(N)
SC:O(1)
"""

#efficient approach is using dutch nationalflag algorithm.
#TC: O(N)
#SC: O(1)
#this is efficient than before method because this algo works in 1 pass rather than 2 pass.

def sort012(a,n):
    low=0
    high=n-1
    mid=0
    while(mid<=high):
        if(a[mid]==0):
            a[low],a[mid]=a[mid],a[low]
            low+=1
            mid+=1
        elif(a[mid]==1):
            mid+=1
        elif(a[mid]==2):
            a[mid],a[high]=a[high],a[mid]
            high-=1
    return a
 
a=[]
n=int(input())
for i in range(0,n):
    x=int(input())
    a.append(x)

sort012(a,n)
for i in range(0,n):
    print(a[i],end=" ")

print()
