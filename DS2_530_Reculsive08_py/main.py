# 재귀 함수 :
# 1. Exit condition 
# 2. Exit 아닐시 data 처리 과정을 정의 
# 3. 자신 호출 
# 4. 완료시 return 처리 과정을 정의 
# 재귀 호출 시점 이후 과정을 다시 정의 내리면. BackTracking !   

def reclusive (num) : 
    if num <=1 : # exit 조건 
        return 1
    else : 
        return reclusive(num-1)*num 
        # 5번) 마지막 호출 시점 return 상태 : (return값=1)*(num=2) 
        # 4번) 마지막-1 호출 시점 return 상태 : (return값 =5번값)*(num=3) = (2)*(3)
        # 3번) 마지막-2 호출 시점 return 상태 : (return값 =4번값)*(num=4) = (6)*(4)
        # 2번) 마지막-3 호출 시점 return 상태 : (return값 =3번값)*(num=5) = (24)*(5)
        # 1번) 최초 호출 후 최종 return 상태 : (return값= 2번값) = (24*5) 



# Callback 함수 
# - 완료시 처리할 과정 + callback 종료 전까지 처리 할 과정
#  두과정을 구분 처리하는게 핵심이라 이해하고, 
#  위 재귀와 같은 값을 얻는 과정을 아래와 같이 구현  

# 1. Controller 함수: 콜백 호출 완료시 return 처리과정을 정의
# 2. Callback 함수 Exit 조건과 아닐시 data 처리 과정을 정의  
# Callback 함수 호출 이후, 조건 처리해 BackTracking 또한 일괄 처리 해 줄 수 있어 보인다. 
def eventController(event, num, callback):
    return callback(event,num) * num  
        # 5번) 마지막 return 상태 : (return값=event:1)*(num=1) 
        # 4번) 마지막-1 return 상태 : (return값 = 5번값)*(num=2) = (1)*(2)
        # 3번) 마지막-2 return 상태 : (return값 = 4번값)*(num=3) = (2)*(3)
        # 2번) 마지막-3 return 상태 : (return값 = 3번값)*(num=4) = (6)*(4)
        # 1번) 최초 호출 후 최종 return 상태 : (return값= 2번값)*(num=5)= (24)*(5) 

def eventHandler01(event, num): 
    if event < num :
        return eventController(event, num-1, eventHandler01)
    else : 
        return event 
        # 5번) 마지막 호출 상태 : eventController(evnet=1, num=1)  
        # 4번) 마지막-1 호출 상태 : eventController(evnet=1, num=2)
        # 3번) 마지막-2 호출 상태 : eventController(evnet=1, num=3) 
        # 2번) 마지막-3 호출 상태 : eventController(evnet=1, num=4) 
        # 1번) 최초 호출 상태 : eventController(evnet=1, num=5) 

print(reclusive(5))
print(eventController(1,5,eventHandler01))