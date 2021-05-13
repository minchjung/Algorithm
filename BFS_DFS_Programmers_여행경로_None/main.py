# 931Dijkstra_BFS[L3]단어변환_py
import heapq 
def solution(tickets):
    # vis = [ 0 ] * (len(tickets)) 
    tickets.sort()
    hp = [[0,"ICN"]]
    heapq.heapify(hp)
    memo=[0]*(10000)
    vis =[0]*(len(tickets))
    while hp : 
        cost, now= heapq.heappop(hp)
        if -cost >= len(tickets)+1 and 0 in vis :
            vis=[0]*(len(tickets))
            continue 
        if -cost == len(tickets)+1 and 0 not in vis : break 
        memo[-cost]= now
        for i in range(len(tickets)):
            if tickets[i][0]!=now: continue  
            if vis[i]!=0 : continue 
            vis[i]=1
            heapq.heappush(hp, [cost-1, tickets[i][1]])
    return memo 

print(solution([['ICN','B'],['B','ICN'],['ICN','A'],['A','D'],['D','A']]))
# print(solution([['ICN','AAA'],['ICN','AAA'],['ICN','AAA'],['AAA','ICN'],['AAA','ICN']]))
# print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
# print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
# print(solution([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))
# print(solution([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))
