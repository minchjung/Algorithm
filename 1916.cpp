
#include<bits/stdc++.h> 
using namespace std; 

#define loop(i,a,b) for(int i=a; i<b ; i++)
#define in1(a) cin >> a 
#define in2(a,b) cin >> a >> b  
#define in3(a,b,c) cin >> a >> b  >> c
#define out1(a) cout << a << "\n" 
#define out2(a,b) cout << a << " " << b << "\n" 
#define out3(a,b,c) cout << a << " " << b << " " << c << "\n" 
#define X first 
#define Y second 
const int MAX = 1e9;

vector<pair<int, int> > edges[1005]; 
int N, M, a, b, c, start, target, ans, dist[1005]; 
priority_queue<pair<int,int> > PQ;

int main(void){
    ios::sync_with_stdio(0); cin.tie(0); 

    in2(N,M);
    loop(i,0,N+1) dist[i]= MAX; // <--- MAX 
    while(M--){
        in3(a,b,c); 
        edges[a].push_back({c,b}); //{cost, node}    
    }
    in2(start, target); 

    PQ.push({0,start}); //{cost, node}
    dist[start] = 0; 

    while(!PQ.empty()){
        auto cur = PQ.top(); PQ.pop(); //lower cost pop out first 
        // current Cost already greater --> Dont need to go further  
        if(dist[cur.Y] < -cur.X) continue; 
        for(auto nxt : edges[cur.Y]){ // Go search what next node is available
            if(dist[nxt.Y] <= dist[cur.Y] + nxt.X) continue;  // Dont try if the cost is already big 
            dist[nxt.Y] = dist[cur.Y] + nxt.X; // Others, Update the lower cost 
            PQ.push({cur.X - nxt.X, nxt.Y}); // and push it into PQ {-cost total, nxtNode} 
            // negative cost gives the lowest one out of PQ first
        }
    }
    out1(dist[target]);
}
