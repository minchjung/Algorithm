def solution(arr):

    num = [int(arr[0])] 
    for i,a in enumerate(arr) : 
        if a == "-" : num.append( -int(arr[i+1]) )
        elif a == "+" : num.append( int(arr[i+1]) )

    N = len(num) 
    num.reverse()
    dp = [[0,0] for _ in range(N)]
    dp[0] = [num[0], num[0]]

    for i in range(1, N) :
        val1 = dp[i-1][0] + num[i]
        val2 = dp[i-1][1] + num[i]
        if num[i] >= 0 :
            dp[i][0] = max(val1, val2)
            dp[i][1] = min(val1, val2)
        else :
            dp[i][0] = max(val1,val2, -(dp[i-1][0] - num[i]), -(dp[i-1][1] - num[i]))
            dp[i][1] = min(val1,val2, -(dp[i-1][0] - num[i]), -(dp[i-1][1] - num[i]))
    return dp[N-1][0]
