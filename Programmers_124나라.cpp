#include<bits/stdc++.h>
using namespace std; 

string solution(int n ){
    string numbers[3] = {"4","1","2"} ; 
    string answer = ""; 

    while(n){
        answer = numbers[ n %3 ]  + answer ; 
        n = n/3 - (n % 3 == 0) ; 
    }
    return answer ;
}