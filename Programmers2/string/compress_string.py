
S = "aabbaccc"
S = "ababcdcdababcdcd"
S = "abcabcdede"
S = "abcabcabcabcdededededede"
S = "xababcdcdababcdcd"
S = 'a'
def solution(S):
    ans = 1e11;  skip = 1; 
    while skip <= len(S)//2 : 
        now = S[:skip]; comp = now
        s =skip; e= s+ skip; cnt = 1
        while e <= len(S) + skip :
            if len(now) > len(S[s:e]) : 
                comp += (str(cnt) + S[s:e]) if cnt !=1 else S[s:e]; break
            if now == S[s:e] : cnt+=1 
            else : 
                comp += (str(cnt)+ S[s:e]) if cnt != 1 else S[s:e] 
                cnt =1
            now = S[s:e]
            s = e 
            e = s + skip
        ans = min(ans, len(comp)) 
        skip+=1
    return 1 if ans == 1e11 else ans
print(solution(S))