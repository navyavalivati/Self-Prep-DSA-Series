#Quick Sort Algorithm
def partition(a,start,end):
    pi=(start-1)
    pivot=a[end]
    for i in range(start,end):
        if(a[i]<=pivot):
            pi+=1
            a[i],a[pi]=a[pi],a[i]
        
    a[pi+1],a[end]=a[end],a[pi+1]
    return (pi+1)

def QuickSort(a,low,high):
    if(len(a)==1):
        return a
    if(low<high):
        pindex=partition(a,low,high)
        QuickSort(a,low,pindex-1)
        QuickSort(a,pindex+1,high)


n=int(input())
a=[]
for i in range(0,n):
    x=int(input())
    a.append(x)

QuickSort(a,0,n-1)
for i in range(n):
    print("%d" % a[i],end=" ")