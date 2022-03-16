# 영어 끝말잇기
def solution(n, w):
    ans = [0,0] 
    _w = [w[0]]

    for i in range(1,len(w)) :
        if w[i] in _w or w[i][0] != _w[-1][-1]: 
            ans = [1+i%n, 1+i//n]; break  
        _w.append(w[i])
    return ans
    