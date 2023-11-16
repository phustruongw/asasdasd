with open('./bộ đề/2022/password/password.inp') as fin:
    s=fin.readline()
def check(s):
    so=0
    chuhoa=0
    chuthuong=0
    for i in range(len(s)):
        if s[i].isupper():
            chuhoa+=1
        elif s[i].islower():
            chuthuong+=1
        elif s[i].isdigit():
            so+=1
    if(so!=0 and chuhoa!=0 and chuthuong!=0):
        return True
    else:
        return False
result=0
for i in range(6,len(s)+1):
    for j in range(len(s)-i+1):
        if (check(s[j:i+j])):
            result+=1
print(result)