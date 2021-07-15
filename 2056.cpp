// 위상정렬 G4  작업2056 
#include<bits/stdc++.h>
using namespace std; 

#define loop(i, a, b) for(int i = a ; i < b ; i++)
#define out1(a) cout << a << " "
#define out2(a, b) cout << a << " " << b 
#define outN  cout << "\n" 
#define in1(a) cin >> a 
#define in2(a, b) cin >> a >> b

#define X first 
#define Y second

int N, a, b, ans; 
vector<int> board [10005]; 
int ansArr [10005]; 
int ind [10005];
int dur[10005];
queue < int > Q;

int main(void){
    
    in1(N); // 입력 값 N 
    loop(i, 1, N+1){ // 1~ N 까지 for loop
        in1(dur[i]); // 첫번째 입력=시간 을 시간 배열에 기록
        in1(a); // 2번째 연결된 선행되야 할 node 갯수 
        loop(j,0,a) {  // 그 갯수 만큼 loop
            in1(b); // 입력 값을 받아 
            board[b].push_back(i); // board에는 선행 노드를 인덱스로 하위 노드를 push back 
        } 
        ind[i] = a ; // 위상 정렬의 indegree 값은 선행되야 할 node 수인 a 입력 값이므로
    } // 현재 i번째 node에 선행 되야할(전입 node ) 수 를 ind에 기록
    loop(i,1,N+1){ // 1부터 기록돼 있기 때문에 1~ N까지 (N+1) loop 
        if(ind[i]==0){
            ansArr[i] = dur[i]; // 하위 노드가 없는 경우 작업 시간을 기록해주고
            Q.push(i);// Q에 담아 준다
        }
    }
    int tem = 0 ; 
    while(!Q.empty()){
        int cur = Q.front(); Q.pop(); 
        for(int nxt : board[cur]){ // 현재 노드에 연결된 하위 노드를 모두 꺼내 시간을 기록,
            ansArr[nxt] = max(ansArr[nxt], ansArr[cur] + dur[nxt]); 
            // 모두 작업 되었다면, 두 값은 동일 하거나 뒤의 값이 크다. 
            if(--ind[nxt] == 0 )  Q.push(nxt); // 선행 작업이 완료됬으면 Q push 
        }
    }
    loop(i,0,N+1) ans = max(ans, ansArr[i]);
    out1(ans);
}

// Gooood 

// #include<bits/stdc++.h>
// using namespace std;
// #define all(v) v.begin(),v.end()
// using ll = long long;

// int main(){
//     ios::sync_with_stdio(!cin.tie(0));
//     int n; cin>>n;
//     int dp[n+1]={},ans=0;
//     for(int i=1;i<=n;i++){
//         cin>>dp[i];
//         int k=0;
//         int t; cin>>t;
//         while(t--){
//             int p; cin>>p;
//             k = max(k,dp[p]);
//         } 
//         dp[i] += k;
//         ans = max(ans,dp[i]);
//     }
//     cout<<ans;
// }