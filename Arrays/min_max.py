"""
Write a function to return minimum and maximum in 
an array. 
Your program should make the 
minimum number of comparisons. 

"""
""" 
As it is mentioned that comparisons should be minimum, comparsions are done in the form of pairs.
So,
when the length of array n is odd then the first element of the array is initialized to m(min) and n(max)
when the n value is even then the m and n are initialized with the min and max of first two elements

and then looping is performed for every pair and comparisons.
"""
def MinMax(a):
    length=len(a)

    if(length%2==0):
        m=max(a[0],a[1])
        n=min(a[0],a[1])
        i=2
    else:
        m=n=a[0]
        i=1
    
    while(i<length-1):
        if(a[i]<a[i+1]):
            m=max(m,a[i+1])
            n=min(n,a[i])
        else:
            m=max(m,a[i])
            n=min(n,a[i+1])

        i+=2

    return (m,n)


a=[]
length=int(input())
for i in range(0,length):
    x=int(input())
    a.append(x)

Max,Min=MinMax(a)

print("Maximum is: ",Max)
print("Minimum is: ",Min)

