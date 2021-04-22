
#include<bits/stdc++.h>
using namespace std; 
// stack 괄호쌍 [균형잡힌 세상]4949_C++
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    while(true){
        string s ; 
        getline(cin, s); 
        if(s ==".") break;
        stack<char> stack ;
        bool valid =true ; 
        for(auto c : s){
            if(c =='(' || c == '[')   stack.push(c);
            else if(c==')'){
                if(stack.empty() || stack.top() !='('){
                    valid =false;
                    break;
                }
                stack.pop();
            }
            else if(c==']'){
                if(stack.empty() || stack.top() !='['){
                    valid=false;
                    break;
                }
                stack.pop();   
            }
       }
        if(!stack.empty()) valid =false;
        if(valid) cout << "yes\n";
        else cout << "no\n";
    }
}