#Data Structure1_203<String>p14_[alphCount]10809
string = input()
arr=[-1]*26
for i,s in enumerate(string) : 
    a = ord(s)-ord('a')
    if arr[a]==-1:
        arr[a]=i
print(*arr)