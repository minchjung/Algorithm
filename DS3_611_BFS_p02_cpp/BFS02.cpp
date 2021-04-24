#include<bits/stdc++.h>
using namespace std; 
string board[101];
int vis[101][101];
int n, m; 
int dx[4] ={0,0,-1,1};
int dy[4] ={-1,1,0,0}; 

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> n >> m ; 
    for(int i =0; i < n; i ++){
        cin >> board[i]; 
    }
    queue < pair<int,int> > q ; 
    q.push({0,0});
    vis[0][0]= 1 ;
    while(!q.empty()){
        auto now = q.front();
        q.pop(); 
        for(int k =0; k < 4; k++){
            int nx = now.first + dx[k];
            int ny = now.second + dy[k];
            if(nx < 0 || nx >= n || ny < 0 || ny >= m || vis[nx][ny]!=0 || board[nx][ny]!='1' ) continue; 
            q.push({nx,ny});
            vis[nx][ny]=vis[now.first][now.second]+1;
        }
    }
    cout << vis[n-1][m-1];
}