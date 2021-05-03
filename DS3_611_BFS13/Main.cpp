// 611<BFS>[S2]11725_cpp
#include<bits/stdc++.h>
using namespace std ; 
vector<int> board[100002];
int vis[100002];
int n,a,b;
int main(){
    cin >> n ; 
    for(int i=1; i<n; i++){
        cin >> a >> b;
        board[a].push_back(b);
        board[b].push_back(a);
    }
    //Just start from 1 as it's assumed 
    queue<int> q;
    q.push(1);
    vis[1]=1;
    //Go search BFS once<--this works since it only has one graph ! 
    while (!q.empty()){
        int now = q.front(); q.pop(); 
        for(auto nxt : board[now]){
            if(vis[nxt]!=0) continue; 
            vis[nxt]=now;
            q.push(nxt);
        }
    }
    for(int i=2; i<=n; i++) cout<< vis[i]<<"\n";
}
