def solution(brown, yellow):
    tot = brown //2 
    w = tot 
    while w and (w-2)*(tot-w) !=yellow:  w-=1 
    
    return [w,tot-w+2]