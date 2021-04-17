/*
Given two arrays a[] and b[] of size n and n respectively.
The task is to find union between these two arrays.

Union of the two arrays can be defined as the set containing distinct elements from both the arrays. 
If there are repetitions, then only one occurrence of element should be printed in union.
Input:
5 3
1 2 3 4 5
1 2 3

Output: 
5

Explanation: 
1, 2, 3, 4 and 5 are the
elements which comes in the union set
of both arrays. So count is 5.
*/
// using mapping to find union of twp arrays.
#include<bits/stdc++.h>
using namespace std;
int main(){
   int n,m;
   cin>>n>>m;
   map<int,int>mp;
   int a[n],b[m];
   for(int i=0;i<n;i++){
       cin>>a[i];
       mp.insert({a[i],i});
   } 
   for(int i=0;i<m;i++){
       cin>>b[i];
       mp.insert({b[i],i});
   }
   int count=0;
   for(auto it=mp.begin();it!=mp.end();it++){
       count++;
   }
   cout<<count<<"\n";
}