//BOJ 입출력연습.2588
#include<bits/stdc++.h>
using namespace std; 
int main(void){
    int num1, num2;  
    cin >> num1 >> num2; 
    cout << num1 *(num2%10)<<"\n";
    cout << num1 *((num2%100)/10)<<"\n";
    cout << num1 *(num2/100) << "\n";
    cout << num1*num2;
}