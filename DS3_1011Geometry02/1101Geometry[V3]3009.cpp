// 1101<Geometry>[V3]3009_cpp
#include<bits/stdc++.h>
using namespace std;
int x[4];
int y[4]; 

int check(int arr[]){
    int ans ; 
    if(arr[0]==arr[1]) ans=arr[2]; 
    else if(arr[0]==arr[2]) ans=arr[1]; 
    else ans = arr[0];
    return ans ; 
}  
int main(){
    int ansX, ansY; 
    for(int i=0; i<3; i++) 
        cin >> x[i] >> y[i]; 
    ansX = check(x);
    ansY = check(y);
    cout << ansX << " "<< ansY ;
}