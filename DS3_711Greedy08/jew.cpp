#include<bits/stdc++.h>
using namespace std;

typedef pair<int, int> pii; 
typedef vector<int> vi; 
typedef long long ll; 
typedef priority_queue<int> pqi; 

#define X first 
#define Y second 
#define loop(i,a,b) for(int i=a; i<b; i++) 

bool border(int r, int c, int N, int M){ return 0 > r || r >= N || 0 > c || c >= M ; }
bool desc(int a, int b) { return a > b ;}

int dx[4] = {0,0,-1,1};
int dy[4] = {-1,1,0,0};

int N, K;
pii dia[300001]; 
int bag[300001]; 

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> N >> K ; 
    loop(i,0,N) cin >> dia[i].X >> dia[i].Y ; 
    loop(i,0,K) cin >> bag[i];
    sort(dia, dia + N, [](pii &a, pii &b){ return a.X == b.X ? a.Y < b.Y : a.X > b.X;}); 
    sort(bag, bag + K, greater<int>());
    
    pqi pq; 
    int idx = 0 ; 
    loop(i,0,N){
        while( idx < K && dia[i].X <= bag[idx]) idx++;
        pq.push(-dia[i].Y);
        while(pq.size() > idx) pq.pop();
    }
    ll ans = 0 ; 
    while(! pq.empty()){
        ans -= pq.top(); pq.pop();
    }
    cout << ans; 
}
