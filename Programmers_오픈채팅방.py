def solution(record):
    idName={}
    temp = []
    for user in record : 
        try : 
            a,b,c  = user.split(" ") 
            idName[b] = c
            if a == 'Enter' : temp.append(b + " Enter")
            elif a == 'Change' : idName[b] = c
        except: 
            a, b = user.split(" ")
            temp.append(b+ " Leave")
    ans2 = [] 
    for info in temp : 
        userID, saying  = info.split(" ") 
        if saying == 'Enter' : 
            ans2.append(idName[userID] + "님이 들어왔습니다.")
        else : 
            ans2.append(idName[userID] + "님이 나갔습니다.")
    return ans2