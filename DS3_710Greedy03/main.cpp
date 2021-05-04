//710<Greedy>[S5]16435_cpp 
#include<bits/stdc++.h>
using namespace std; 
int N,L,j=0, h[10001] ;
int main(){
    cin >> N >> L ;  
    for(int i=0; i<N; i++) scanf("%d",&h[i]);
    sort(h,h+N); 
    while(j<N){
        if(L >=h[j]) L++;
        j++;
    }
    cout << L; 
}