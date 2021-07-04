#include<bits/stdc++.h>
using namespace std; 

stack<pair <int, char> > st; 
string ss ; 
int main(){
    int ans = 1 ; 
    cin >> ss ;
    // Stack에 Pair {max경우의수, char} push 
    for(int i = 0 ; i < ss.size() ; i++){
        if(ss.at(i)=='d') st.push({10,ss.at(i)}); 
        else st.push({26, ss.at(i)});
    }

    while(!st.empty()){
        auto cur = st.top(); st.pop(); // pop 해서 꺼냄
        if(st.empty()){  // 꺼내고 stack empty 면  
            ans*= cur.first; // 마지막 값으로 ans update 후
            break;  // break
        } 
        // 현재 cur 문자와 stack.top 과 비교해 연속된 같은 문자시
        if(cur.second == st.top().second){ 
            auto tem =st.top(); st.pop(); // stack 최상단을 pop해서 max경우의수-1 해준다
            st.push({tem.first-1, tem.second}); // 그리고 다시 push
        }
        ans *= cur.first; // 현재 max 경우의수를 ans에 곱해서 update
    }
    cout << ans ; 
} 