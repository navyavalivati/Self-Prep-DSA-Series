
/*
You are given a list of n-1 integers and these integers are in the range of 1 to n. There are no duplicates in the list. One of the integers is missing in the list. Write an efficient code to find the missing integer.
Example: 


Input: arr[] = {1, 2, 4, 6, 3, 7, 8}

Output: 5

Explanation: The missing number from 1 to 8 is 5



Input: arr[] = {1, 2, 3, 5}

Output: 4

Explanation: The missing number from 1 to 5 is 4

*/
//Method 1 is to use summation formula
/*
Approach: The length of the array is n-1. So the sum of all n elements, i.e sum of numbers from 1 to n can be calculated using the formula n*(n+1)/2. Now find the sum of all the elements in the array and subtract it from the sum of first n natural numbers, it will be the value of the missing element.

#include<bits/stdc++.h>
using namespace std;
int main(){
    int n;
    cin>>n;
    int a[n];
    for(int i=0;i<n;i++){
        cin>>a[i];
    }
    int tot=(n+1)*(n+2)/2; 
    for(int i=0;i<n;i++){
        tot-=a[i];
    }
    cout<<tot<<"\n";

}
*/
/* MODIFICATION OF OVERFLOW
Approach: The approach remains the same but there can be overflow if n is large. In order to avoid integer overflow, pick one number from known numbers and subtract one number from given numbers. This way there won't have Integer Overflow ever.

*/
#include<bits/stdc++.h>
using namespace std;
int main(){
    int n;
    cin>>n;
    int a[n];
    for(int i=0;i<n;i++){
        cin>>a[i];
    }
    int total=1;
    for(int i=2;i<=(n+1);i++){
        total+=i;
        total-=a[i-2];
    }
    cout<<total<<"\n";
}
