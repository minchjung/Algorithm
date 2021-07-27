def solution(progress, speeds):

    cntArr = [0]*(len(progress))
    ans = []
    cnt = 0 

    for i in range(len(progress)): 
        while progress[i] + speeds[i]*cnt < 100 : cnt +=1 
        cntArr[i] = cnt 

    tem = cntArr[0]
    cntArr.append(1000)
    cnt2 = 1 
    for i in range(1,len(cntArr)):
        if tem == cntArr[i] : 
            cnt2 +=1 
        else : 
            tem = cntArr[i]
            ans.append(cnt2)
            cnt2 = 1 
    return ans