#include <bits/stdc++.h>
using namespace std;

long long arrK[10001]; 
int main(){
    long long start = 1; 
    long long K, N, end; 
    cin >> K >> N ; 

    for(int i=0; i< K; i++) 
        cin >> arrK[i];
    sort(arrK,arrK + K);
    end = arrK[K-1];
    while (start <= end){
        long long cnt= 0 ; 
        long long mid = (start + end) / 2 ; // 중간 값 설정 

        for(int i=0; i<K; i++)
            cnt += (arrK[i]/mid);
        
        if(cnt >= N)  start = mid+1;
        else  end = mid-1; 
    }
    cout << end; 
}