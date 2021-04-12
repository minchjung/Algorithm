#Data Structure1_203<String>p19_[Suffix]11656
string = input()
arr =[] 
for i in range(len(string)):
    arr.append(string[i:])
arr.sort()
for a in arr : 
    print(a)