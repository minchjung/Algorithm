#include <bits/stdc++.h>
using namespace std;

long long arrN[1000001];
int main(){
    ios::sync_with_stdio(0), cin.tie(0);
    long long N, M, end; 
    long long start = 0 ; 

    cin >> N >> M ;
    for (int i =0 ; i < N; i++)
        cin >> arrN[i];   
    end = *max_element(arrN, arrN + N);

    while(start <= end){
        long long cm = 0 ; 
        long long mid = (start + end)/2; 

        for(int i = 0 ; i < N; i++){
            if(arrN[i] - mid >=0 ) 
                cm += (arrN[i]- mid); 
        }
        if(cm >= M) start = mid + 1; 
        else end = mid - 1;
    }
    cout << end; 

}