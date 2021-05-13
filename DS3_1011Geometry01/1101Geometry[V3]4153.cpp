// 1101<Geometry>[V3]4153_cp
#include<bits/stdc++.h>
using namespace std; 

int main(){
    int a, b, c ; 
    cin >> a >> b >> c; 
    while (a && b && c){
        if (a*a + b*b == c*c || a*a + c*c == b*b || b*b + c*c == a*a) 
            cout << "right" << "\n"; 
        else cout << "wrong" << "\n";
        cin >> a >> b >> c ; 
    }
}