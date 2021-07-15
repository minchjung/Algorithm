// 1200 위상정렬 G2 2623_음악프로그램
#include<bits/stdc++.h>
using namespace std; 

#define loop(i, a, b) for(int i=a; i< b; i++)
#define in1(a) cin >> a 
#define in2(a,b) cin >> a >> b 
#define out1(a) cout << a << "\n"
#define out2(a, b) cout << a << " "<< b << "\n ";

int N, M, a, b, c;
vector<int> arr[1005];
vector<int> ans;
int ind[1005];
queue<int> Q; 

int main(void){
    in2(N,M);
    loop(i,1,M+1){ //위상 정렬 setting 작업
        in1(a); // i번째 pd가 가진 정보 수 a
        in1(b); // a 정보 최상위 노드 b
        a--;
        while(a--){ // a개 만큼의 정보 loop
            in1(c); // b의 하위 노드를
            arr[b].push_back(c); // push
            ind[c]++; // 상위 노드가 있는 c를 그때마다 ind +1
            b=c; // 하위 노드가 그 다음번 상위 노드
        }
        //arr[K] = {K라는 노드에 연결된 모든 하위노드 정보}
    }
    loop(i,1,N+1) 
        if(!ind[i]) Q.push(i); //상위 노드가 없는 최상위 노드를 Q push 
    while(!Q.empty()){
        int cur = Q.front(); Q.pop();
        ans.push_back(cur); //ans 저장 (상위 노드가 없는 순으로 저장된다)
        for(int nxt : arr[cur]) //현재 노드에 연결된 모든 하위 노드를 탐색
            if(--ind[nxt] ==0) Q.push(nxt); // 간선 수 하나 지우는데, 0이되면 
            //(현재 상황에서 최상위 노드와 같으므로 Q push)
    }
    if(ans.size() != N) out1(0); //그래프에 사이클이 있으면 위상 정렬 불가
    else
        loop(i,0,ans.size()) out1(ans[i]); // 아니면 순서대로 출력
}