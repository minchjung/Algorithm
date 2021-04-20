# 500<BruteForece>p04_[일곱난쟁이]2309_py
dwarf = [int(input()) for _ in range(9)] 
dwarf.sort()
def calculate(ans):
    for i in range(len(dwarf)-1): 
        hap=sum(dwarf) -dwarf[i] 
        for d in dwarf[i+1:]:
            if hap - d ==100 : 
                ans.remove(dwarf[i])
                ans.remove(d)
                return ans
for i in calculate(ans = dwarf): 
    print(i)
