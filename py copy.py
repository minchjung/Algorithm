def solution(price,money,count):
    arr = [price*i for i in range(count+1)]
    ans =sum(arr[:count+1]) - money 
    if ans <= 0 : ans =0 
    return ans 
solution(3,20,4)