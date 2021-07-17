#include<bits/stdc++.h>
using namespace std ; 

typedef vector<pair<int, int> >vpii;
typedef long long ll ;
#define loop(i,a,b) for(int i=a; i< b; i++) 
#define in1(a) cin >> a 
#define in2(a,b) cin >> a >> b 
#define in3(a,b,c) cin >> a >> b >> c 
#define out1(a) cout << a << "\n"
#define out2(a,b) cout << a << " " << b << "\n"

const ll INF = LLONG_MAX; // <-- INF value has to be bigger than 1e10 
int N, M, a, b, c ;
vpii bus[505];
ll dis[505]; // <-- distance shoud be long long 
bool negCycle = false; 

int main(void){
    ios::sync_with_stdio(0); cin.tie(0);
    loop(i,0,505) dis[i] = INF;
    in2(N,M);

    while(M--){
        in3(a,b,c); 
        bus[a].push_back({b,c});
    }
    dis[1]=0;
    loop(busNUM,0,N+1){
        loop(cur,1,N+1){
            for(auto nxt : bus[cur]){ 
            // MUST check whether this node is not INF  -> means that Graph is disconnected 
                // So you cannot go to this cur node from start point 
                if(dis[cur] != INF && dis[nxt.first] > dis[cur] + nxt.second){ 
                    // if it's in the same graph with the start point and min cost to pass thru nxt node  
                    dis[nxt.first] = dis[cur] + nxt.second; // update min value to nxt node 
                    if(busNUM == N) negCycle = true;  // it has more to update than total number of nodes 
                    //  ==> means negative cycle 
                    // you dont need to break here ;; since its the last loop
                }
            }
        }
    }
    if(negCycle) out1(-1); // negative cycle 
    else loop(i,2,N+1) out1((dis[i]==INF? -1:dis[i]));
    // dis[node] = INF means disconnected => print -1 or print dis[node] as min dsitance
    
}