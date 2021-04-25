// 000[basic][벌집]2292_p03_cpp
#include<bits/stdc++.h>
using namespace std; 
int main(void){
    int n;
    cin >> n; 
    int i = 1;   
    n--; 
    while(n>0){
        n =n -6*i;
        i++;
    }
    cout << i ;
}