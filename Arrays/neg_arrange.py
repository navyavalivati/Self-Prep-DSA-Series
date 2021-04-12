"""
An array contains both positive and negative numbers in random order. Rearrange the array elements so that all negative numbers appear before all positive numbers.
Examples : 

Input: -12, 11, -13, -5, 6, -7, 5, -3, -6
Output: -12 -13 -5 -7 -3 -6 11 6 5
Note: Order of elements is not important here.

"""
#one approach is to simply use inbuilt sort function as it is mentioned that order of elements is not important here.

"""
a=[]
n=int(input())
for i in range(0,n):
    x=int(input())
    a.append(x)

a.sort(reverse=False)
for i in a:
    print(i,end=" ")
print()

"""
#Another approach is to use partition technique of quick sort algo.
#TC: O(N) SC: O(1)
def neg_arrange(a,n):
    j=0
    for i in range(0,n):
        if(a[i]<0):
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
            j+=1

    return a

n=int(input())
a=[]
for i in range(0,n):
    x=int(input())
    a.append(x)
neg_arrange(a,n)

for i in range(0,n):
    print(a[i],end=" ")