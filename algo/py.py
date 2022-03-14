from itertools import combinations
def solution(rel):
    C = len(rel[0])
    col = list(range(1,C+1)) 
    ans =[]
    for i in range(1,C):
        for comb in combinations(col,i):
            boo = False 
            for aa in range(len(ans)) : 
                t = [False]*len(ans[aa])
                for aaa in range(len(ans[aa])) :
                    if ans[aa][aaa] in comb : t[aaa]=True 
                if False not in t : boo = True ; break 
            if boo : continue 

            D = dict()
            for r in rel :
                key = ''; val =''
                for idx, content in enumerate(r):
                    if idx+1 in comb : key += content 
                    else : val += content 
                D[key] = val 
            if len(D) == len(rel) :
                ans.append(comb)
    return 1 if not len(ans) else len(ans)

r = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
r = [['a', 'aa'], ['aa', 'a'], ['a', 'a']] 
# r = [ ["a","1","aaa","c","ng"],
# ["a","1","bbb","e","g"],
# ["c","1","aaa","d","ng"],
# ["d","2","bbb","d","ng"]];
a = solution(r)
print(a)