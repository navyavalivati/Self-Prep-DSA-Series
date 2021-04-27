"""
Given an array and a number k where k is smaller than size of array, we need to find the k’th smallest element in the given array. It is given that all array elements are distinct.

Examples:  

Input: arr[] = {7, 10, 4, 3, 20, 15} 
k = 3 
Output: 7

Input: arr[] = {7, 10, 4, 3, 20, 15} 
k = 4 
Output: 10 

"""
#Bruteforce approach is to sort the array and print the kth index element of the array.
"""
a=[]
n=int(input())
for i in range(0,n):
    x=int(input())
    a.append(x)
k=int(input())
a.sort(reverse=False)
print(a[k-1])
"""
