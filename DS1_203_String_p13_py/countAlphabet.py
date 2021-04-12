#Data Structure1_203<Stack>p13_[알파벳개수]10808
string = input()
arr=[0]*26
for s in string : 
    a = ord(s)-ord('a')
    b = string.count(s)
    arr[a]=b
print(*arr)