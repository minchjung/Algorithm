import math 
# 주차요금 계산 
def solution(fees, records):
    info = dict() 
    cars = [] 
    for rec in records : 
        t,p,i = rec.split(" ")
        a, b = map(int,t.split(":"))
        try : info[p].append(a*60+b)
        except : info[p] = [a*60+b]
    for key, val in info.items() : 
        if len(val) % 2 : info[key].append(23*60+59)
        cars.append(key)
    cars.sort()
    ans = [0]*len(cars)
    for i, car in enumerate(cars) :
        tot = 0
        for t in range(0,len(info[car]),2):
            tot += info[car][t+1] - info[car][t]
        if tot <= fees[0] : ans[i]= fees[1]
        else : ans[i] = fees[1] + math.ceil( (tot-fees[0])/fees[2] )*fees[3]

    return ans 

# f = [180, 5000, 10, 600]
# r = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
# f = [120, 0, 60, 591]
# r = ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]
# f = [1, 461, 1, 10]
# r = ["00:00 1234 IN"]
# a = solution(f,r)