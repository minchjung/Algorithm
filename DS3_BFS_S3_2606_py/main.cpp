#include<bits/stdc++.h>
using namespace std; 

vector<vector<int>> vec ; 
int main(void){
    int n, k,a,b; 
    cin >> n >> k ; 
    for(int i=0; i <n;i++){
        cin >> a >> b ; 
        vec[a].push_back(b);
        vec[b].push_back(a);
        cout << vec[a][b] << vec[b][a] ;      
    } 
}