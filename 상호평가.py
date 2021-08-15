def grade(target):
  ans=''
  if target >= 90 : ans = 'A'
  elif target >=80 : ans = 'B'
  elif target >=70 : ans = 'C'
  elif target >=50 : ans = 'D'
  else : ans ='F'
  return ans    

def solution(scores):
  ans=''
  student = [ [scores[j][i] for j in range(len(scores[i])) ] for i in range(len(scores))] 
  for i, score in enumerate(student) : 
    tot = sum(score)
    sub = len(score) 
    if score[i] == max(score) or score[i] == min(score) : 
      if score.count(score[i]) <= 1 : 
        tot -= score[i] 
        sub -= 1
    ans += grade(tot/sub)
  return ans 

print(solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]))
# solution([[70,49,90],[68,50,38],[73,31,100]])
# solution([[50,90],[50,87]]);
# def solution(scores):
#   ans = [] 
#   for i in range(len(scores)):
#     tem = []
#     self, cnt = 0, 0
#     tot = 0 ; 
#     for j in range(len(scores[i])):
#       if i ==j : self= scores[j][i]
#       tem.append(scores[j][i])  
#     tot = sum(tem)
#     student=[self, max(tem), min(tem)]
#     if student[0] == student[1] or student[0] == student[2]:
#       for ele in tem:
#         if cnt > 1 : break 
#         if ele == self : cnt+=1
#     if cnt <= 1 : 
#       ans.append(grade( (tot-student[0])//(len(scores[i])-1) ))
#     else : ans.append(grade( tot//len(scores[i]) ))
  
#   return ''.join(ans) 

# print(solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]))
# # solution([[70,49,90],[68,50,38],[73,31,100]])
# # solution([[50,90],[50,87]]);