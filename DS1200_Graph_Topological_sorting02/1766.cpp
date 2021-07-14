// G2 문제집 1766
#include<bits/stdc++.h>
using namespace std; 

#define loop(i,a,b) for(int i=a ; i<b ; i++)
#define deb(a) cout << (a) << " " 

int N, M, a, b; 
vector<int> board [32005];
vector<int> ans;
int indeg [32005]; 
priority_queue<int> PQ;

int main(void){
    ios::sync_with_stdio(0); cin.tie(0);
    cin >> N >> M ; 

    loop(i,0,M){
        cin >> a >> b ; 
        board[a].push_back(b); 
        indeg[b]++;
    }
    loop(i,1,N+1) if(indeg[i] == 0) PQ.push(-i);
    while(!PQ.empty()){
        int cur = -PQ.top(); PQ.pop();
        ans.push_back(cur);
        for(auto nxt : board[cur]){
            indeg[nxt]--;
            if(indeg[nxt]==0) PQ.push(-nxt);
        }
    }
    loop(i,0,ans.size()) deb(ans[i]);
}