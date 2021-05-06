# 710<Greedy>[V3]11034_py
while True: 
    try:
        a,b,c = map(int, input().split())
        print(max(b-a-1,c-b-1))
    except: break