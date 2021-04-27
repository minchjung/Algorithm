#include<bits/stdc++.h>
using namespace std ;

int dx[4] = {0,0,1,-1};
int dy[4] = {1,-1,0,0};

int BFS(int n, int m , int k){
    // initialize board and vis for each case 
    int board[501][501];
    int vis[501][501];
    int num =0 ; 
    for(int i = 0 ; i < n ; i++){
        fill(board[i],board[i]+m,0); // fill method 
        fill(vis[i],vis[i]+m,0);  
    }
    for(int i =0; i<k ; i++){
        int a, b; 
        cin >> b >> a ;
        board[a][b]=1;
    }
    for(int i = 0 ; i < n ; i ++){
        for(int j =0; j< m ; j++){
            if(vis[i][j]!=0 or board[i][j]!=1) continue;
            num++; 
            queue < pair <int,int> > q ; 
            q.push({i,j}); 
            vis[i][j]=1 ; 
            while(!q.empty()){
                auto now = q.front(); q.pop(); 
                for(int d =0; d<4 ; d++){
                    int nx = now.first + dx[d];
                    int ny = now.second + dy[d];
                    if(nx<0 || nx>=n || ny<0 || ny>=m) continue; 
                    if(vis[i][j]==1 || board[i][j]==0) continue; 
                    q.push({nx,ny});
                    vis[nx][ny]=1;
                }
            }
        }
    }
    return num ; 
}
int main(void){
    int t,n,m,k ; 
    cin >> t ; 
    for(int i = 0 ; i < t; i++){
        cin >> m >> n >>k ;
        int ans = BFS(n,m,k);
        cout << ans<< "\n";
    }
}
