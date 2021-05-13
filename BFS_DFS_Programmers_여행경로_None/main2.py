def solution(tickets):
    tickets = sorted(tickets, reverse=True) 
    memo=[0]*(len(tickets)+1)
    vis=[0]*(len(tickets))
    def backTrack(k,port):
        if k==len(tickets)+1 and 0 not in vis :  return  
        for i in range(len(tickets)): 
            if tickets[i][0]!=port:continue
            if vis[i]!=0 : continue
            memo[k]=tickets[i][1]
            vis[i]=1 
            backTrack(k+1,tickets[i][1])
            vis[i]=0 
    memo[0]="ICN"
    backTrack(1,"ICN")
    return memo 
# print((solution([['ICN','B'],['B','ICN'],['ICN','A'],['A','D'],['D','A']])))
# print(solution([['ICN','AAA'],['ICN','AAA'],['ICN','AAA'],['AAA','ICN'],['AAA','ICN']]))
# print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
# print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
# print(solution([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))
# print(solution([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))
