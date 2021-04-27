/*
Given an array of positive integers and many queries for divisibility. In every query Q[i], we are given an integer K , we need to count all elements in the array which are perfectly divisible by K.

 

Example 1:

Input:
N = 6
A[] = { 2, 4, 9, 15, 21, 20}
M =  3
Q[] = { 2, 3, 5}
Output:
3 3 2
Explanation:
Multiples of '2' in array are:- {2, 4, 20}
Multiples of '3' in array are:- {9, 15, 21}
Multiples of '5' in array are:- {15, 20}
 

Example 2:

Input:
N = 3
A[] = {3, 4, 6}
M = 2
Q[] = {2, 3}
Output:
2 2

*/
#include<bits/stdc++.h>
using namespace std;
vector<int> countMultiples(int a[],int q[],int n,int m);
int main(){
    int t;
    cin>>t;
    while(t--){
        int n,m;
        cin>>n>>m;
        int q[m],a[n];
        for(int i=0;i<n;i++){
            cin>>a[i];
        }
        for(int i=0;i<m;i++){
            cin>>q[i];
        }
        vector<int> ans=countMultiples(a,q,n,m);
        for(auto it:ans){
            cout<<it<<" ";
        }
        cout<<"\n";
    }
}
vector<int> countMultiples(int A[], int Q[], int N, int M) {
   int MAX=*max_element(A,A+N);
   vector<int>res;
   int count[MAX+1]={0};
   int ans[(MAX+1)*sizeof(int)]={0};
   for(int i=0;i<N;i++){
       ++count[A[i]];
   }
   for(int i=1;i<=MAX;i++){
       for(int j=i;j<=MAX;j+=i){
           ans[i]+=count[j];
       }
   }
   for(int i=0;i<M;i++){
       res.push_back(ans[Q[i]]);
   }
   return res;
}