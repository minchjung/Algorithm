# 710<Greedy>[S2]11501_py
T =int(input())
for _ in range(T): 
    N =int(input())
    price = list(map(int, input().split()))
    maxP=0
    ans=0
    # 거꾸로 탐색해주고 max값을 항상 비교해 갱신한다 
    for i in range(len(price)-1,-1,-1):
        maxP=max(maxP,price[i])
        ans+=(maxP-price[i])
    print(ans)
    # 10^6번의 최대연산 케이스 =>for문 index조회만 1초 (O[N])
    # 나머지 연산까지 1000ms+알파의 시간 복잡도 
    # 제한시간 5초로 충분  (greedy특징) 