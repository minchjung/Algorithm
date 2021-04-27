// 000[mid]3273
#include<bits/stdc++.h>
using namespace std; 

int arr[100001]; 
vector<int> vec;
int main(void){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int n,x,num,ans=0 ; 
    cin >> n ; 
    for(int i=0; i<n; i++){
        cin >> num;
        arr[num]++;
        vec.push_back(num);
    }
    cin >> x ;
    for(int i=0; i < vec.size() ; i++){
        if(arr[vec[i]]>=1 && arr[abs(x -vec[i])]>=1){
            ans++;
            arr[vec[i]]--;
            arr[abs(vec[i]-x)]--;
        } 
    }
    cout << ans ; 
}   