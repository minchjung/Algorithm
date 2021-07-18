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
const int INF = 1e9;

int N, E, u, v, w, root, dist[20005];
vector< pair<int,int> > edges[20005]; 

int main(void){
    in2(N,E);
    in1(root); // root
    while(E--){
        in3(u,v,w); // depart -> arrive, weight 
        edges[u].push_back({w,v}); //{cost, node}
    }
    loop(i,0,N+1) dist[i] = INF; // MAX  
    
    priority_queue<pair<int, int> >PQ; 
    dist[root] =0; // start root distance = 0 
    PQ.push({-dist[root], root}); //{-cost , node}

    while(!PQ.empty()){
        auto cur = PQ.top(); PQ.pop();
        if(dist[cur.Y] < -cur.X) continue;  // cost is good for now => continue 
        for(auto nxt : edges[cur.Y]){ // if its not => search next node from current 
            if(dist[nxt.Y] < dist[cur.Y] + nxt.X) continue;  // if next node is good  ==> continue
            dist[nxt.Y] = dist[cur.Y] + nxt.X;  // or update min cost to dist[nextnode]
            PQ.push({ -nxt.X + cur.X, nxt.Y }); // and push into PQ as its one partial of min path from root 
        }
    }
    loop(i,1,N+1){
        if(dist[i] == INF) out1("INF");
        else out1(dist[i]); 
    }
}