def solution(id_list, report, k):
    cnt = [0]*len(id_list); 
    ans = cnt[:]; idx = dict()
    board = [ [] for _ in range(len(id_list))]
    
    for i, id in enumerate(id_list) : idx[id] = i
    for r in range(len(report)) :
        a,b = report[r].split(" ")
        if idx[b] in board[idx[a]] : continue 
        board[idx[a]].append(idx[b]) 
        cnt[idx[b]]+=1 
    for a in range(len(board)) : 
        for b in board[a] : 
            if cnt[b] >= k : ans[a]+=1
    return ans

# id = ["muzi", "frodo", "apeach", "neo"]	
# rep = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi", "muzi frodo"]
# k=2

# id = ["con", "ryan"]	
# rep = ["ryan con", "ryan con", "ryan con", "ryan con"]
# k = 3
# a = solution(id, rep, k)
# print(a)