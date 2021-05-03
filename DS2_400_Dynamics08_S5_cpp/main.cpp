// 400<Dynamics>[S5][Four Squares]17626_cpp
#include<bits/stdc++.h>
using namespace std ; 
int dp[50001];
int main(){
    int n; dp[1]=1; 
    cin >> n ; 
    for(int i=2; i<=n; i++){
        dp[i]=50000; 
        for(int j=1; j*j<=i; j++)
            dp[i] = min(dp[i],dp[i-j*j]+1);
    } 
    cout << dp[n];
}