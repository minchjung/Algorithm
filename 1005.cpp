// 1200 그래프_위상정렬 [G3]1005 ACM Craft
#include<bits/stdc++.h>
using namespace std; 

typedef long long ll;
typedef vector<int> vi;
typedef vector<long long> vl;
#define loop(i,a,b) for(int i=a; i <b; i++)
#define in1(a) cin >> a 
#define in2(a,b) cin >> a >> b 
#define out1(a) cout << a <<"\n"; 


int T, N, K, W, a, b;
void goTopo(void){
    //every vector and array has to be initialized to 0, righ here
    vl arr[1005]={}; 
    ll ans[1005]={};
    ll dur[1005]={};
    ll ind[1005]={};
    queue<int> Q;

    in2(N,K);// N = num of building, K = num of edges 
    loop(i,1,N+1) in1(dur[i]); // time of each building to construct
    loop(i,1,K+1){ // get all info of every edge 
        in2(a,b); // a is prerequisite of b 
        arr[a].push_back(b);
        ind[b]++; // b +1 since it has prereq, a
    }
    in1(W);// last building to exit 
    loop(i,1,N+1){ // To find the topest 
        if(ind[i] ==0){ //since it has no prereq, means that the one is the topest
            Q.push(i); //push it into Q
            ans[i] =dur[i]; // Memo the time to build of it
        }
    }
    while(!Q.empty()){ //BFS
        int cur = Q.front(); Q.pop(); 
        if(cur == W) break; // if its last one =>  break
        for(auto nxt : arr[cur]){ // or get rid of a number of edges
            ans[nxt] = max(ans[nxt], ans[cur] + dur[nxt]); //Choose acculmulated building time 
            if(--ind[nxt]==0) Q.push(nxt);// and if nxt is now the topest => Q push
        }
    }
    out1(ans[W]); //get print answer
}
int main(void){
    ios::sync_with_stdio(0); cin.tie(0);
    in1(T);
    loop(i,0,T) goTopo(); // Loop to test case
    
    return 0;
}
// Issue to Check 
// Initalize array and vector not on global
// Q has to be clear if it exit befor pop everything out 
// => simply declare Q when it nees  
// => queue<> Q;
