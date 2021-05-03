// <Greedy>[V2]5585_cpp
#include<bits/stdc++.h>
using namespace std; 
int main(void){
    int coin[6]={500,100,50,10,5,1};
    int money,ans=0; 
    cin >> money ; 
    money=1000-money;
    for(int i=0; i<6;i++){
        while(money-coin[i]>=0){
            money-=coin[i];
            ans+=1;
        }
    }
    cout<< ans;
}
