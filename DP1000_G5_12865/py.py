N, K = map(int, input().split())
board = [  list(map(int, input().split()))  for _ in range(N) ]
board.sort(reverse=True)

dp = [ [0]*(K+1) for _ in range(N+1) ]
for i in range(1,N+1) :
    curW = board[i-1][0]
    curV = board[i-1][1]
    for sackW in range(K+1) :
        if curW > K : dp[i]=dp[i-1]
        if curW > sackW : continue  
        dp[i][sackW] = max(dp[i-1][sackW-curW]+curV, dp[i-1][sackW])
print(dp[N][K])