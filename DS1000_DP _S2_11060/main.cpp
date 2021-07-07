#include<bits/stdc++.h> 
using namespace std; 

vector<int> board; 
int dp[1010];
int N,  MAX = 1000*1000; 

int getAns(int end){

    int minT= MAX;
    if (end < 0) return 0 ; 
    if (end + board[end] >= N) {
        dp[end] = 1 ;
    }else{
        for(int i = end+1 ; i <= end + board[end]; i++)
            minT = min(minT, dp[i]) ;
        dp[end] = minT +1 ;
    }
    getAns(end-1); 
    return 0 ; 
}

int main(){

    ios::sync_with_stdio(0); 
    cin.tie(0);
    int a, cnt=0; 
    cin >> N; 
    
    for(int i = 0 ; i< N ; i++){
        cin >> a ; 
        board.push_back(a);
        dp[i]=MAX; 
    }
    getAns(N-1);
    
    if (dp[0] >= MAX) cout << "-1"; 
    else cout << dp[0] ; 
}