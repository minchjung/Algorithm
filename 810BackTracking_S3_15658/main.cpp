#include<bits/stdc++.h>
using namespace std; 
int opUsed[50], opAns[20],N;
long maxAns=-1000000000;
long minAns=1000000000;
vector<int>op(50,0);
vector<long>number;

long calculate(){
    long num = number[0];
    for(int i=0; i<N-1; i++){
        int tem=opAns[i];
        if(tem==1) num+=number[i+1];
        else if(tem==2) num-=number[i+1];
        else if(tem==3) num*=number[i+1];
        else{
            if(num<0){
                num*=-1;
                num/=number[i+1];
                num*=-1;
            }
            else num/=number[i+1];
        }
    }
    return num; 
}
int backTrack(int k){
    if(k==N-1){
        long tem = calculate(); 
        maxAns = max(maxAns,tem);
        minAns = min(minAns,tem);
        return 0;  
    }
    for(int i=0; i<4*N; i++){
        if(opUsed[i]!=0) continue; 
        opUsed[i]=1; 
        opAns[k]=op[i]; 
        backTrack(k+1);
        opUsed[i]=0;
    }
}
int main(void){
    int num, cnt; 
    cin >> N; 
    for(int i=0; i<N; i++){
        cin >> num; 
        number.push_back(num);
    }
    for(int i=0; i<N; i++){
        cin >> cnt; 
        for(int j=0; j<cnt;j++)
            op.push_back(i+1);
    }
    backTrack(0); 
    cout << maxAns << "\n" << minAns;
}

