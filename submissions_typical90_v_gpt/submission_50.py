A,B,C=map(int, input().split())
prev=[A,B,C]
cut=1
while True:
    prev.sort()
    if prev[0]==0:
        break
    elif prev[1]%prev[0]==0 and prev[2]%prev[0]==0:
        cut=prev[0]
        break
    else:
        prev=[prev[0],prev[1]-prev[0],prev[2]-prev[0]]

ans=(A+B+C)//cut-3
print(ans)