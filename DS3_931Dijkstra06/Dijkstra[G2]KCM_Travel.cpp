#include<bits/stdc++.h>
using namespace std;
const int INF = 1000*105; 
vector<pair<int, pair<int, int>>>board[105];
int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int T,N,M,K,u,v,c,d,ans; 
    // int time[105];
    cin >> T; 
    for(int i = 0 ; i <T ; i++){
        cin >> N >> M >> K ; 
        for(int j=1x; j<K; j++) board[j].clear();
        for(int j=0; j<K; j++){
            cin >> u >> v >> c >>d ; 
            board[u].push_back({d,{c,v}}) ; 
        }
        priority_queue<pair<int, pair<int,int>>> pq; 
        pq.push({0,{0,1}});
        ans=INF;
        // fill_n(time,105,INF); 
        while(!pq.empty()){
            int nowTime = pq.top().first; 
            int nowCost = pq.top().second.first; 
            int nowNode = pq.top().second.second;  
            pq.pop(); 
            if(nowNode==N && M >=nowCost){
                ans =min(ans,nowTime);
                continue; 
            }
            for(auto nxt : board[nowNode]){
                int nxtTime = nxt.first; 
                int nxtCost = nxt.second.first; 
                int nxtNode = nxt.second.second; 
                if ( M < nowCost + nxtCost ) continue; 
                if (ans <= nowTime + nxtTime) continue; 
                pq.push({nowTime+nxtTime, {nowCost+nxtCost, nxtNode}});
            }
        }
        if(ans==INF) cout << "Poor KCM\n"; 
        else cout << ans<<"\n";         
    }
} 
// import heapq 
// import sys
// T = int(sys.stdin.readline())
// for _ in range(T):  
//     N,M,K = map(int, sys.stdin.readline().split())
//     board = [[] for _ in range(K+1)] 
//     for _ in range(K): 
//         depart,arrive,c,t = map(int, sys.stdin.readline().split())
//         board[depart].append([t,c,arrive])
//     hp=[]
//     heapq.heappush(hp,[0,0,1])
//     ans= 100*1000
//     while hp : 
//         nowTime, nowCost, nowNode = heapq.heappop(hp)
//         if nowNode == N and M >= nowCost : 
//             ans = min(ans,nowTime)
//             continue 
//         for nxtTime, nxtCost, nxtNode in board[nowNode]:
//             if M < nowCost + nxtCost : continue 
//             if ans <= nowTime + nxtTime : continue 
//             heapq.heappush(hp, [nowTime + nxtTime, nowCost+nxtCost ,nxtNode]) 
//     if ans== 100*1000: sys.stdout.write("Poor KCM"+'\n')
//     else: sys.stdout.write(str(ans)+'\n')                 