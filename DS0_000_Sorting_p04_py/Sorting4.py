# Sorting04 단어정렬 py _ 우선순위 
# 1. 길이 , 2. 알파벳 
n  = int(input())
string = [] 
for _ in range(n): 
    s = input().strip() 
    l = len(s)
    string.append((l,s)) 
string = list(set(string)) 
# 묶어서 1차로 길이, 2차로 String 알파벳 정렬 
string.sort(key=lambda x : (x[0],x[1]))
for s in string :
    print(s[1])