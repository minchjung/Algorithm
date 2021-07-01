#include <bits/stdc++.h>
using namespace std;

pair <long long, long long> pairNum;
void task01(long long k ){
  long long digit = 1;
  long long leng = 9;
  long long tot = 0;
  while(true){
    tot += digit*leng;
    if(k <=tot){
      tot -= digit*leng;
      digit--;
      break;
      }
    digit ++; 
    leng *=10;
  }
  pairNum = make_pair(digit, tot);

}
int main() {
  long long N, K, digit, startN=1 ;
  cin >> N >> K; 
  task01(K);
  if(N==1 && K==1){
      cout<< 1;
      return 0;
  }

  digit = pairNum.first;
  K -= pairNum.second;

  while(digit--) startN *=10;
  startN += K/(pairNum.first+1);

  if(startN > N){
    cout << -1;
    return 0 ; 
  } 
  if(K%(pairNum.first+1)==0){ 
    startN --;
    cout << to_string(startN)[pairNum.first];
  }
  else{ 
    cout << to_string(startN)[K%(pairNum.first+1)-1];
  }
  return 0; 
}
