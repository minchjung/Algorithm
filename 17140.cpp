#include <bits/stdc++.h>
using namespace std; 
#define loop(i,a,b) for(int i=a ; i < b; i++)
#define in1(a) cin >> a 
#define in3(a,b,c) cin >> a >> b >> c 
#define out1(a) cout << a << '\n'
//17140 이차원배열과 연산 
int A[100][100];
int X, Y, K, T, R, C;
int a, b, c;

int main(){
  in3(X,Y,K);
  X--; Y--; R = 3; C = 3;

  loop(i,0,3){
    loop(j,0,3) in1(A[i][j]);
  }

  while(T < 100){
    if(A[X][Y] == K){
      out1(T); 
      return 0;
    } 
    if(R >= C){
      map<int, int> cntNum;
      loop(r, 0, R){
        loop(c, 0, C){
          if(!A[r][c]) continue; 
          cntNum[A[r][c]] +=1; 
        }
        vector <pair<int,int>> vec;
        for(auto key : cntNum) vec.push_back({key.second, key.first});
        sort(vec.begin(), vec.end());

        C = max(C, (int)vec.size()*2);
        int len = min(50, (int)vec.size()*2);
        loop(i,0,len){
          A[r][i*2] = vec[i].second;
          A[r][i*2+1] = vec[i].first;
        }
        loop(i,len,100) A[r][i] = 0;
      }
    }
    else{
      map<int, int> cntNum;
      loop(c, 0, C){
        loop(r, 0, R){
          if(!A[r][c]) continue; 
          cntNum[A[r][c]] +=1; 
        }
        vector <pair<int,int>> vec;
        for(auto key : cntNum) vec.push_back({key.second, key.first});
        sort(vec.begin(), vec.end());

        R = max(R, (int)vec.size()*2);
        int len = min(50, (int)vec.size()*2);
        loop(i,0,len){
          A[i*2][c] = vec[i].second;
          A[i*2+1][c] = vec[i].first;
        }
        loop(i,len,100) A[i][c] = 0;
      }
    }
    T++; 
  }
}