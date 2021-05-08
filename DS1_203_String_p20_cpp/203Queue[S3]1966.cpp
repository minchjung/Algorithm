// 203<Queue>[S3]1966_cpp
#include<bits/stdc++.h>
using namespace std; 

int main(void){
    int T,N,target,priority;
    cin>>T;
    for(int i=0 ; i<T ; i++){
        cin >> N >> target; 
        queue<pair<int,int>> q; 
        priority_queue<int> pq; 
        for(int j=0; j<N; j++){
            cin >> priority; 
            q.push({priority, j});
            pq.push(priority);
        }
        int cnt=1; 
        while(!q.empty()){
            auto tem = q.front(); q.pop();
            if(tem.second==target && tem.first==pq.top()){
                cout << cnt << "\n";
                break;
            }
            if(tem.first == pq.top()){
                pq.pop();
                cnt++;
            } 
            else q.push(tem);
        }
    }
}