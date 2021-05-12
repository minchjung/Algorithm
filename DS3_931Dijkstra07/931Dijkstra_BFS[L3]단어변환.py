# 931Dijkstra_BFS[L3]단어변환_py
import heapq
def solution(begin, target, words): 
    vis=[0]*(len(words))
    pq=[]
    pq.append([0,begin])
    heapq.heapify(pq)
    ans = 0 
    while pq : 
        cost,now =heapq.heappop(pq)
        if now == target : 
            ans = cost 
            break 
        for i in range(len(words)): 
            if vis[i] != 0 : continue
            temCnt=0 
            for j in range(len(now)): 
                if now[j] == words[i][j] : temCnt+=1                     
            if temCnt != len(now)-1: continue 
            vis[i]=1 
            heapq.heappush(pq, [cost+1,words[i]])
    return ans    
print(solution("hit","cog",	["hot", "dot", "dog", "lot", "log", "cog"])) 