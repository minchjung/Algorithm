// <Dynamics>[피보나치함수]3273_silv3[+6]
#include<bits/stdc++.h>
using namespace std; 
int dp[50];
int main(void){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int T,n ; 
    cin >> T ; 
    dp[0]=0, dp[1]=1;
    for(int i =2 ; i < 42 ; i++) dp[i]=dp[i-2]+dp[i-1];
    for(int i = 0 ; i < T ; i++){
        cin >> n ; 
        if(n==0) cout << "1 0\n";
        else if(n==1) cout << "0 1\n"; 
        else cout<< dp[n-1] <<" "<< dp[n]<<"\n";
    }

}   