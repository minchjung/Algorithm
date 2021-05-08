// 710<Greedy_Sorting>[S5]_10989_cpp
#include<bits/stdc++.h>
using namespace std; 
int arr[10001];
int main(){
    ios_base::sync_with_stdio(0); //<--이거 안넣으면 시간초과 
    cin.tie(0);
    int n, num; 
    cin >> n; 
    for(int i=0; i< n; i++){
        cin >> num ; 
        arr[num]++;
    }
    for(int i=1; i<10001; i++){
        while(arr[i]--)
            cout << i<< "\n";
    }
}
