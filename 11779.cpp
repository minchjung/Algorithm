#include<bits/stdc++.h>
using namespace std; 

#define loop(i,a,b) for(int i=a; i< b; i++)
#define in2(a, b) cin >> a  >> b 
#define in3(a, b, c) cin >> a  >> b >> c  
#define out1(a) cout << a << " "
#define out1N(a) cout << a << "\n"
#define out2(a,b) cout << a << " " << b << "\n"
#define out3(a,b,c) cout << a << " " << b << " " << c << "\n"
#define X first
#define Y second
typedef vector<pair <int, int>> vii ; 
const int INF = 1e9; 

int N, M, a, b, c, start, target;
int dist[1005], pre[1005]; 
vii edges[1005];
vector<int> path; 

int main(void){
    in2(N,M); 
    while(M--){
        in3(a,b,c);
        edges[a].push_back({c,b}); // { cost, node }
    }
    in2(start, target); 
    loop(i,0,N+1) dist[i] = INF; 
    priority_queue<pair<int,int> > PQ ; 
    dist[start] = 0; 
    PQ.push({ dist[start], start }); // { cost, node}
    while(!PQ.empty()){
        auto cur = PQ.top(); PQ.pop();
        if(dist[cur.Y] < -cur.X) continue;
        loop(i,1,N+1){   
            for(auto nxt : edges[cur.Y]){
                if(dist[nxt.Y] <= dist[cur.Y] + nxt.X ) continue; 
                dist[nxt.Y] = dist[cur.Y] + nxt.X ; 
                pre[nxt.Y] = cur.Y; 
                PQ.push({ cur.X - nxt.X , nxt.Y}); 
            }
        } 
    }
    int _end = target; 
    while(_end!=start){
        path.push_back(_end);
        _end = pre[_end]; 
    }
    path.push_back(_end);
    reverse(path.begin(), path.end());
    
    out1N(dist[target]);
    out1N(path.size());
    loop(i,0,path.size()) out1(path[i]);
}
