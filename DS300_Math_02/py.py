# 000f<sorting>[v1]1259
a = ""; 
while a!="0" : 
    a = input() 
    b = True
    for i in range(int(len(a)/2)): 
        if a[i] != a[len(a)-i-1]: 
            print("no")
            b = False
            break 
    if a!="0"and b : print("yes")
