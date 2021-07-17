#include<bits/stdc++.h>
using namespace std; 

typedef vector<pair<int, int> > vpii; 
#define X first 
#define Y second 
#define loop(i,a,b) for (int i=a; i<b; i++) 
#define in1(a) cin >> a 
#define in2(a,b) cin >> a >>b 
#define in3(a,b,c) cin >> a >> b >> c  
#define out1(a) cout << a << "\n" 
#define out2(a,b) cout << a << " "<< b << "\n"  

const int MAX = 1e9; 
int TC, N, M, W, a, b, c, ans ;
int main(void){
    ios::sync_with_stdio(0); cin.tie(0);
    in1(TC); 
    while(TC--){
        vpii board[505] = {}; // board[node] = { {adjcent node1, distance1}, {adj node2, dist2}, ...}
        int ans[505] = {MAX}; // All distance initialize to INF or MAX

        in3(N,M,W);
        loop(i,0,M){
            in3(a,b,c); 
            board[a].push_back({b,c}); // undirected edges 
            board[b].push_back({a,c});
        }
        loop(i,0,W){
            in3(a,b,c);
            board[a].push_back({b,-c}); // directed edges (warmhole -> negative distance)
        }
        bool check = false; 
        ans[1] = 0; // start from any node and let distance[start] = 0
        loop(nodeNum,1,N+2){ // you count a number of nodes (just over a number of total nodes ) 
            loop(cur,1,N+1){ // current node 
                for(auto nxt : board[cur]){ // Search all adjcent node from current node
                    // if distance of next node is bigger than the one via current node
                    if(ans[nxt.X] > ans[cur] + nxt.Y){ 
                        ans[nxt.X] = ans[cur] + nxt.Y;  // should be updated for minimum distance
                        if(nodeNum == N+1) check = true;  // if you can update the distance of (N+1) node 
                                                    // which is not available unless it has negative cycle
                    }
                }
            }
        }
        if(check) out1("YES"); 
        else out1("NO");
    }
}