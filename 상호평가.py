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
