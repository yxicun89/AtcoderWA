n = int(input())

score1 = [0] * n
score2 = [0] * n

inputCP = input().split()
if inputCP[0] == '1' :
        score1[0] = int(inputCP[1])
else :
        score2[0] = int(inputCP[1])
        
for i in range(1,n,1) :
    inputCP = input().split()
    if inputCP[0] == '1' :
        score1[i] = score1[i-1] + int(inputCP[1])
        score2[i] = score2[i-1]
    else :
        score2[i] = score2[i-1] + int(inputCP[1])
        score1[i] = score1[i-1]
    
q = int(input())

AB = []

for j in range(q):
    inputLR = input().split()
    A = score1[int(inputLR[1])-1] - score1[int(inputLR[0])-2]
    B = score2[int(inputLR[1])-1] - score2[int(inputLR[0])-2]
    
    AB.append(str(A)+' '+str(B))
    

for i in range(q):
    print(AB[i])