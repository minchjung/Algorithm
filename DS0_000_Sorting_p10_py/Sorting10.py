# Sorting10 통계학 2108 py 
from collections import Counter
# roundUp 함수
# python round함수 사사오입에 따른 2.5등의 짝수 정수는 round 버림 
# => 반올림 함수 따로 구현.
def roundUp(number):
    if number - int(number) >= 0.5: 
        return int(number)+1
    else: 
        return int(number)

# input setting 
n = int(input())
num = [int(input()) for i in range(n)] # 총 숫자 정보를 담은 배열 

# 1.avg
avg = sum(num) / n
ans=0 # 평균값 
if avg < 0 : # 음수일 경우 
    avg*=-1  # 양수로 바꿔서 반올림 
    ans = -1*roundUp(avg) # return에서 다시 음수로
else: # 양수면 그대로 반올림
    ans = roundUp(avg)
print(ans)  #평균 값 출력

# 2.mid 
num.sort() # 숫자 배열 오름차순 
if len(num) % 2 ==0:  # 숫자 total 갯수=짝수면 
    print(len(num)//2 - 1) # 길이의 반에서 인덱스 1앞 = 중위값
else : print(num[len(num)//2])  # 홀수면 2로 나눈 몫 =중위값

# 3.freq
count = Counter(num) # 카운터 함수 정렬 
freq = count.most_common() # 빈도수 가장 높은것들 모두 freq에 담아
if len(freq)>=2:  # 2개 이상이면 
    print(freq[1][0]) # [1][0] 두번째 숫자 출력  (value : count)
else: # 1개면 
    print(freq[0][0])  # 첫번째 숫자 출력  

# 4.scope
if len(num)<=1: # 숫자 only 1개 
    print(0) # 범위 = 0  출력
else: # 숫자 총 2개 이상
    print( max(num)-min(num) ) # 최대값-최소값 = 범위 출력