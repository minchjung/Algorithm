#include <bits/stdc++.h>
using namespace std; 

int N; 
int inOrder[100001]; 
int postOrder[100001]; 
int idx[100001];
void preOrder(int is, int ie, int ps, int pe){
	if (is > ie || ps > pe) return;
	int move = idx[postOrder[pe]]; 
	cout << postOrder[pe] << " ";

	preOrder(is, move -1, ps, ps + move -is -1);
	preOrder(move + 1, ie, ps + move -is, pe - 1);
}

int main(){
	ios::sync_with_stdio(0);
	cin.tie(0);
	cin >> N;

	for (int i = 0; i < N; i++)
		cin >> inOrder[i];

	for (int i = 0; i < N; i++){
		cin >> postOrder[i];
		idx[inOrder[i]] = i; 
	}
	preOrder(0, N, 0, N);
}