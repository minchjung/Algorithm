def solution(info,query) : 

    iboard=[i.split() for i in info]
    qboard =[]
    ans = [0]*len(query)

    for q in query : 
        for i in range(4) : 
            q = q.replace("and", "")
        qboard.append( q.split())

    for k in range(len(qboard)) :
        cur = qboard[k]
        for inf in iboard : 
            if int(inf[4]) < int(cur[4]) : continue 
            cnt = 1
            for i in range(len(inf)) :
                if cur[i] != '-' and cur[i] != inf[i] : break
                cnt += 1
            if cnt >=5 : ans[k]+=1
    # print(ans)
    return  ans

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
solution(info, query)