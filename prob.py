
def solution(arr):
    strNum = list(map(str, arr))
    strNum.sort(key = lambda x : x*5, reverse=True)
    print(strNum)
    return str(0) if strNum[0] == str(0) else "".join(strNum)

print(solution([0,0,0,0,0,0]))
# print(solution([3, 30, 34, 5, 9]))