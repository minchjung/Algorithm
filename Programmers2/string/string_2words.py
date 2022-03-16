# 뉴스 클러스터링 
import math, re 
def solution(s1,s2):
    s1 = [ s1[i:i+2].lower() for i in range(len(s1)-1) if not re.findall('[^a-zA-Z]+', s1[i:i+2]) ]
    s2 = [ s2[i:i+2].lower() for i in range(len(s2)-1) if not re.findall('[^a-zA-Z]+', s2[i:i+2]) ]

    inter = set(s1) & set(s2)
    union = set(s1) | set(s2)

    _inter = sum([ min(s1.count(_i), s2.count(_i)) for _i in inter ])
    _union = sum([ max(s1.count(_u), s2.count(_u)) for _u in union ])
    return math.floor(65536*(_inter/_union)) if _union else 65536


# import math 
# # 뉴스 클러스터링 
# def solution(s1,s2):
#     s1 =s1.lower(); s2 = s2.lower(); 
#     alph = list(map(chr,list(range(97,123))))

#     A=[]; w = s1[0] 
#     for i in range(1,len(s1)): 
#         A.append(w+s1[i])
#         w = s1[i]
#         if A[-1][0] not in alph or A[-1][1] not in alph : A.pop()
    
#     B=[]; w=s2[0]
#     for i in range(1,len(s2)):
#         B.append(w+s2[i])
#         w=s2[i]
#         if B[-1][0] not in alph or B[-1][1] not in alph : B.pop()

#     _A = dict(); _B = dict();  
#     for a in A:
#         _A[a] = _A[a]+1 if a in _A else 1 
#     for b in B :     
#         _B[b] = _B[b]+1 if b in _B else 1 
    
#     inter = 0 
#     for key, val in _A.items():
#         if key in _B : inter += min(val, _B[key])

#     uni = len(A) + len(B) - inter
#     return math.floor(65536*(inter/uni)) if uni else 65536



