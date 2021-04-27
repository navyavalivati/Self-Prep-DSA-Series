/*
Given an array of n integers and q queries. Write a program to find floor value of mean in range l to r for each query in a new line.

Example 1:

Input : Arr[] = {1, 2, 3, 4, 5}, Q = 3
queries[] = {0, 2, 1, 3, 0, 4}
Output : 2 3 3
Explanation:
Here we can see that the array of 
integers is [1, 2, 3, 4, 5].
Query 1: L = 0 and R = 2
Sum = 6
Integer Count = 3
So, Mean is 2
Query 2: L = 1 and R = 3
Sum = 9
Integer Count = 3
So, Mean is 3
Query 3: L = 0 and R = 4
Sum = 15
Integer Count = 5
So, the Mean is 3.
So, In the end, the function will 
return the array [2, 3, 3] as an answer.
Example 2:

Input : Arr[] = {6, 7, 8, 10}, Q = 2
queries[] = {0, 3, 1, 2}
Output : 7 7

*/
#include<bits/stdc++.h>
using namespace std;
class Solution{
    public:
        vector<int> findMean(int a[],int queries[],int n,int q){
            vector<int>res;
            int sum=0,count=0;
            for(int i=0;i<q;i+=2){
                int L=queries[i];
                int R=queries[i+1];
                sum=0;
                count=0;
                for(int j=L;j<=R;j++){
                    sum+=a[j];
                    count++;
                }
                int x=sum/count;     //math.floor(sum/count);
                res.push_back(x);
            }
            return res;
        }
};
int main(){
    int t;
    cin>>t;
    while(t--){
        int n,q;
        cin>>n>>q;
        int a[n+1],queries[2*q+1];
        for(int i=0;i<n;i++){
            cin>>a[i];
        }
        for(int i=0;i<2*q;i++){
            cin>>queries[i];
        }
        vector<int>ans;
        Solution ob;
        ans=ob.findMean(a,queries,n,2*q);
        for(auto i:ans){
            cout<<i<<" ";
        }
        cout<<"\n";
    }
}