#include<bits/stdc++.h>
using namespace std;
//      board,     최소거리누적memo, 노드방문정memo 
int board[130][130], dist[130][130], vis[130][130];
int dx[4]={1,-1, 0, 0};
int dy[4]={0, 0, 1,-1};
int N; 
int cnt=1; 

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    N=125;
    while(N){
        memset(vis,0,sizeof(vis));
        cin >> N ;
        //board & dist배열 초기화
        for(int i=0; i<N; i++){
            for(int j=0; j<N; j++){
                int a ;
                cin >> a ;
                board[i][j]=a; 
                dist[i][j]=1300;
            }
        }
        // cpp, priority_queue 문법 <자료형,Container,자료형의 정렬방법> 
        priority_queue <pair <int, pair<int,int>>, vector<pair <int, pair<int,int>>>, greater<pair <int, pair<int,int>>>> pq;
        // priority q 초기값 설정 {시작값,{0,0}} && dist 누적거리 메모 
        dist[0][0]=board[0][0];
        pq.push({ dist[0][0], {0,0} });
        // BFS with priority => dijkstrat 
        while(!pq.empty()){
            // 노드중 짧은 거리 우선 순위로 pop
            auto now = pq.top(); pq.pop();
            int w = now.first;
            int x= now.second.first;
            int y =now.second.second;
            for(int i=0; i<4; i++){
                int nx= x + dx[i];
                int ny= y + dy[i];
                // 범위 입구 컷 
                if(nx<0 || nx >=N || ny<0 || ny >=N || vis[nx][ny]!=0) continue; 
                int nxtW = dist[x][y] + board[nx][ny];
                // 해당노드를 거쳐갈때 누적거리가 이미 저장된 거리보다 크면 입구 컷 
                if(dist[nx][ny] < nxtW) continue;
                // 그게 아니면 update 시켜주고, 해당 노드 방문처리 후,힙큐 저장,
                dist[nx][ny]=nxtW;
                vis[nx][ny]=1;
                pq.push({nxtW, {nx,ny}});
            }
        }
        if(N==0) break; 
        cout << "Problem " << cnt<<": "<<dist[N-1][N-1]<<"\n";
        cnt++;
    }
    return 0;
}
//  함수로 쪼개서 실행하면 런타임에러 =(Double Free) 발생 => 메모리 덮어쓰기 오류 
//  포인터 ref 넘겨봐도 왜 안되는지 모르것다 ㅠ 