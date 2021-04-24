// 611<BFS>[그림]1926_c++
#include <bits/stdc++.h>
using namespace std;
int board[501][501];
int vis[501][501];
int dx[4] = {0,0,1,-1};
int dy[4] = {1,-1,0,0};
int n,m;
int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> n >> m ; 
    for(int i =0 ; i < n; i ++)
        for(int j =0 ; j < m; j ++) 
            cin >> board[i][j];  
    int maxPic = 0 ;
    int picNum = 0 ;

    for(int i =0 ; i < n; i ++){
        for(int j =0 ; j < m; j ++) {
            if(board[i][j]==0 || vis[i][j] ) continue;
            picNum++;
            queue < pair<int, int> > q ;
            vis[i][j]=1;
            q.push({i,j});
            int area = 0 ; 
            while(!q.empty()){
                area ++ ;
                pair <int, int> now = q.front();
                q.pop();
                for(int k =0; k < 4 ; k++){
                    int nx = now.first + dx[k];
                    int ny = now.second + dy[k];
                    if(nx < 0 || nx >= n || ny < 0 || ny >= m) continue;  
                    if (board[nx][ny] !=1 || vis[nx][ny])continue;
                    q.push({nx,ny});
                    vis[nx][ny] = 1 ; 
                }            
            }
            maxPic = max(maxPic, area);
        }
    }
    cout << picNum << "\n" <<  maxPic; 
} 