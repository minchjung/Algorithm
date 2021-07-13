def cal(n1,n2):
    tem=set()
    tem.add(n1+n2)
    tem.add(n1-n2)
    tem.add(n1*n2)
    if n2 !=0:
        tem.add(n1//n2)

    return tem

def start(arr1,arr2):
    setarr=set()
    for a in arr1 : 
        for b in arr2: 
            setarr = setarr |(cal(a,b))
            setarr = setarr |(cal(b,a))
    return setarr

def solution(n,target): 
    result =[set() for i in range(9)]
    result[1].add(n)
    idx= 0
    if target ==0 : 
        return -1 
    if target == n :
        return 1 
    for i in range(2,9):
        for j in range(1,i//2+1):
            result[i] = (start(result[j],result[i-j]))
            result[i].add(int(str(n)*i))
            if target in result[i]:
                return i
    return -1