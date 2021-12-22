## [1. Matrix 90도 회전](https://github.com/minchjung/algorithm_js/blob/main/rotateMatrix.js)  

#### :pushpin: 문제 [T22]
90도, 180도 270도 360도 회전을 n번 했을때  
회전된 행렬을 반환 
#### :pushpin: Soln1 90도 회전
규칙1 : 행-> 열, 열->행   
규칙2 : 행 처음 -> 열 끝   
규칙3 : 행 끝 -> 열 처음  
#### :pushpin: Soln2 n번 회전 
1번 회전 : soln1 1번 진행   
2번 회전 : soln1 2번 진행  
3번 회전 : soln1 3번 진행  
4번 회전 : 회전 필요x 그대로!  
=> 4의 나머지로 해결!  

## [2. Matrix 테두리 회전](https://github.com/minchjung/algorithm_js/blob/main/spiralTraversal.js)  
#### :pushpin: 문제[T23]
1. 바깥쪽 테두리를 순회하고   
2. 안쪽 테두리를 순회  
3. 모든 요소를 테두리 순회로 이어 붙여 return 

#### :pushpin: Soln1 
1. 테두리 순회    
2. 바깥 테두리 끝 => 안쪽 테두리로 변경   
3. 재귀로 진행   
#### :pushpin: Soln2  재귀 
1. 재귀 break : 이어 붙인 길이 == 행x열  
2. 테두리 변경 : 재귀 시작 지점으로 왔을때 변경 
3. 구현 
```js  
재귀함수(r, 시작r, 끝r, c, 시작c, 끝c){
  ans += board[r][c]
  if(이어 붙인 ans길이 === N*M) return 
  if(오른쪽 가야할때) c++;
  if(아래쪽 가야할때) r++;
  if(왼쪽 가야할때) c--;
  if(위쪽 가야할때) r--;
  if(시작지점 일때) return 재귀함수(r+1,시작r+1,끝c-1, c+1, 시작c+1, 끝c-1);
  재귀함수(r,c,시작r,끝r,c,시작c,끝c);
}
```
#### :pushpin: Overview
　 테두리 순회 여러 방식이 있다.  
　 위와 비슷한 방식에서 테두리가 끝날 때마다 행렬을 바꿔 주거나  
　 아니면, vis 맵을 두어, BFS, DFS 변형을 해도 좋지만,(경계 조건 추가)    
 　어차피 테두리가 오른쪽, 아래쪽, 왼쪽, 위쪽으로 방향이 바뀔때의 조건이 필요했던 것 같다.  
 　결국 방향 변경 4조건, 테두리 끝 지점일때 안쪽 테두리로 변경 조건, 그리고 모두 순회 했을때 그만 두는 조건     
 　이 조건 처리 조합을 잘 해주면 되는데, 재귀로 위 조건을 걸어 주는게 현재 (내 깜냥으로 ㅠ) 제일 나아 보인다.  
 　  

## [3. 기수정렬 with 음수](https://github.com/minchjung/algorithm_js/blob/main/radixSort.js)  
#### :pushpin: 문제[T24] 
수가 나열된 배열을 정렬 
#### :pushpin: Soln1
1. 가장 큰 수의 자릿수를 구한다.  
2. [0~9] 까지 버켓 배열을 생성  
3. 자릿수 간격으로 탐색 => 1, 10, 100, ...  
4. 그 때마다, 배열을 처음부터 순회  
5. 그 자리수의 숫자를 버켓 배열의 인데스로 해당 숫자를 삽입  
`buket[자릿수] = arr[i]`    
6. arr배열을 모두 순회 후, bucket 배열을 바탕으로 다시 정렬한다.    
7. 1번의 가장 큰 자릿 수까지 모두 반복되면 arr배열이 모두 정렬됨  
#### :pushpin: Soln2  
음수는 bucket 배열을 하나 더 두어서     
양수 정렬과 함께 진행 하면 된다.    
다만, 6번의 배열을 다시 재정렬 할때  
음수 bucket 먼저 해주고    
인덱스를 이어 받아 양수로 정렬!  
## [4. Matrix 최소거리]()    
#### :pushpin: 문제[T25]
2차원 행렬 에서 
시작점에서 타켓까지 최소거리를 구한다.    
#### :pushpin: Soln 
전형적인 BFS 또는 DFS 최소거리 값으로 구할 수 있다.  
#### 🔗 관련 문제 link 
[게임맵 최단거리](https://github.com/minchjung/Algorithm/wiki/Test_set01#crossed_fingers-%EA%B2%8C%EC%9E%84-%EB%A7%B5-%EC%B5%9C%EB%8B%A8%EA%B1%B0%EB%A6%AC)

## [5. 연속된 부분 배열의 최대합](https://github.com/minchjung/algorithm_js/blob/main/LSCS.js)    
#### :pushpin: 문제[T26]
연속된 부분 배열의 최대합을 구하는 케이스  
#### :pushpin: Soln1 O(N^3)
```js
let maxAns = 0;
for(let i = 0; i < arr.length; i++){
	let ans = [];
	for(let j = i; j < arr.length; j++){
		ans = [...ans, arr[j]]
		maxAns = Math.max(maxAns, ans.reduce((tot,ele) => tot + ele,0))
	}
}

```
#### :pushpin: Soln2 O(N) by dp 
1. 배열의 요소 N 개를 처음 부터 탐색   
2. 현재 인덱스의 최대합(부분해) 결정.     
3. 방식은 이전 최대합 과 현재 요소와 최대합을 더한 값을 비교    
4. 현재 요소 = 음수, 더하지 않는 것이 최대 해    
5. 음수들을 누적 더해야 할 경우가 있기 때문에  
6. 현재 요소가 음수 일 경우 dp의 해는 0 + 음수 로 처리  
    
## [6. Matrix 상하좌우 퍼뜨리기](https://github.com/minchjung/algorithm_js/blob/main/Toy/gossip_protocol.js)
#### :pushpin: GossipProtocol문제[T27]
시작지점에서 상하좌우 1칸씩 퍼뜨려, 빈칸 모든 곳을 퍼뜨리는데 걸리는 최소 시간 
#### :pushpin: Soln 
최소 거리 구하기 BFS, DFS로 쉽게 구할 수 있다. 

## [7. Matrix 상하좌우 퍼뜨리기](https://github.com/minchjung/algorithm_js/blob/main/Toy/robotPath2.js)  
#### :pushpin: robotPath2 문제[T28]
시작지점에서 해당 조건으로 이동 할 수 있고,    
목표 지점 까지 이동하는 최소 동작 수    
90도 회전이 동작 카운트에 포함  
#### :pushpin: Soln 
최소 거리 구하기 최소 비용 구하기와 동일한 로직  
조건만 추가해 주고 그때 마다 이동 회수를 따로 설정해 주면 됨  
단, 처음 시작할때 이동 방향에 따라 직진 하는 동작 과     
탐색 도중에 직진 하는 동작의 차이가 있음 (조건으로 해결주면 됨)    

## [8. 최대힙, 이진트리, binary Heap](https://github.com/minchjung/algorithm_js/blob/main/Toy/binaryHeap.js)  
#### :pushpin: binaryHeap 문제[T29]
배열의 오름차순 정렬을 이진트리를 활용해 정렬 O(logN) 
#### :pushpin: Soln  
하나씩 새로운 배열에 추가!    
parent Node = (현재 node -1)/2 가 존재하면     
비교해서 parent 보다 현재 node 값이 크면    
swap !!  둘의 값을 교체    
parent 노드가 없거나, 값이 더 작아서 최대힙이 만족 될때까지   
계속해서 거슬러 올라가 주면 된다.    
배열의 모든 요소를 동일하게 탐색하면   
새로운 배열은 최대힙이 구현된다.  


## [10. Segment tree](https://github.com/minchjung/algorithm_js/blob/main/Toy/segment_tree.js)  
#### :pushpin: rangeMinimum 문제[T31]
정렬되지 않은 배열에서, 주어진 구간에서 대한 가장 작은 값을 return 

#### :pushpin: Soln  
1. Tree setting  
- 트리 배열의 길이 = 깊이 * 2    
- 리프 도달까지 자식 노드 좌우로 분할   
- 좌우 자식의 값 중 작은 값 선택    
- 리프 도달시, 리프 자신의 값 할당   
2. 쿼리 수행 트리 탐색  
- 범위내의 최소값 찾기   
- 범위 벗어 낫을시 : 최대값 (무시 값)    
- 범위 내 있을때만 : 현재 노드의 값(최소값) 리턴   
- 걸친 범위는 두 범위에만 해당 될 수 있도록 : 반으로 나눠서 좌우 탐색  
- 탐색 결과의 최소 값만을 선택 할당 
- 끝   
## [11. Histogram](https://github.com/minchjung/algorithm_js/blob/main/Toy/32_histogram.js)  

## [12. Logest Common Subsequence ](https://github.com/minchjung/algorithm_js/blob/main/Toy/segment_tree.js)  
#### :pushpin: LCS 문제[T33]
문자열 2개의 부분 문자열(subseqeunce) 중 서로 같은 부분 문자열의 길이가 가장 큰 값을 return 
#### :pushpin: Soln  
1. DP-2차원 O[MN] by 2차원 dp
2. 이중 for문   
- i=j=0 으로 인덱싱-1로 조회 주의 !  
- 첫째: 세로문자 와 가로 문자 쭈욱 비교 중 서로 일치 하면 위 값+1 
- 둘째: 일치 하지 않으면, 위값, 옆값 비교 선택 

## [13. Logest Icreasing Subsequence](https://github.com/minchjung/algorithm_js/blob/main/Toy/segment_tree.js)  
#### :pushpin: LIS 문제[T34]
배열의, 부분 수열 중 오름 차순 정렬된 가장긴 부분 수열의 길이를 return 
#### :pushpin: Soln  
1. DP 선형 O[N^2] by multiple loop
2. 이중 for문   
- dp[i] = 픽한 숫자 arr[i] 보다 탐색중인 arr[j] 수가 크면    
- dp[i] = 픽한 숫자의 해dp[i]  와 dp[j]+1 현재 탐색 중인 해를 붙인 해를 비교 해서 큰값 선택   
- 아니면 무시

## [14. DP 3가지 케이스](https://github.com/minchjung/algorithm_js/blob/main/Toy/segment_tree.js)  
#### :pushpin: uglyNumber 문제[T35]
2,3,5로 나눠 떨어지는 수를 차례로 정렬했을때, 주어진 Target번째에 해당하는 uglynumber를 return 

#### :pushpin: Soln  
1. DP 선형
2. 선형 for문     
- [n2,n3,n5] = [dp[i2]x2, dp[i3]x3, dp[i5]x5]    
- n2,n3,n5 가장 작은 값이 현재 dp[i]에 할당 되어야할 해!   
- 가장 작은 값에 해당 하는 세개 2,3,5 인덱스는 모두 +1로 하나 증가 시켜 주면 끝     

## [15. 분할 정복 ](https://github.com/minchjung/algorithm_js/blob/main/Toy/segment_tree.js)  
#### :pushpin: ClosePairsofPoints 문제[T36]
주어지는 배열 = [ [x1,y1],[x2,y2],[x3,y3],[x4,y4],[x5,y5] ]에서 두 점사이 거리가 가장 작은 값을 return   

#### :pushpin: Soln  
<1> x좌표 기준 정렬 후 이분 탐색 
1. 분할 하지 못할때 까지 분할 
 - 못하는 케이스 1 ) 두 점만 존재 
 - 못하는 케이스 2 ) 세 점 존재  
 - 각각의 케이스 마다 두 점 사이의 거리를 구해 return (최소값만)  
2. 분할 가능 하면 반으로 나눠 왼, 오른쪽 계속 분할    
3. 재귀 return 값들을 비교해 최소값만 update at `d`  
<2> 분류2 - 재귀 탐색 과정 줄이기 
4. 이진 탐색 후, 탐색할 배열을 filtering !  
5. 지금의 최소 값 보다 작은 점은 x좌표 sorting에서 뺀다.  
<3> 분류3 - y좌표 기준 정렬 후 완전 탐색  
1. 지금의 최소 값 보다 작은 두 점은 계산 하지 않고, 가능한 점만 계산 
2. 최소값 비교 update   
끝  
## [16.Dp CoinChange]  
#### 📌 coninChange : 문제[T37]
1. Dp
##[17. DP ]()
#### 📌 coninChange : 문제[T38]
##[18. DP ]()
#### 📌 coninChange : 문제[T39]
##[19. DP ]()
#### 📌 coninChange : 문제[T40]
##[20. DP ]()
#### 📌 coninChange : 문제[T41]
##[21. DP ]()
#### 📌 coninChange : 문제[T42]
##[22. DP ]()
#### 📌 coninChange : 문제[T43]
##[23. DP ]()
#### 📌 coninChange : 문제[T44]

##[24. DP ]()
#### 📌 coninChange : 문제[T45]
