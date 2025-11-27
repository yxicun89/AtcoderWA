
#Queue

def initialize():

    global head,tail

    head=tail=0



def isEmpty():

    global head,tail

    return head==tail



def isFull():

    global head,tail,Max

    return head==(tail+1)%Max



def enqueue(x):

    global head,tail,Max

    if isFull():

        return "エラー"

    Q[tail]=x

    if tail+1==Max:

        tail=0

    else:

        tail+=1

def sentou(x):

    global head,tail,Max

    if isFull():

        return "エラー"

    Q[(head-1)%Max]=x

    head=(head-1)%Max



def deque():

    global head,tail,Max

    if isEmpty():

        return "エラー"

    x=Q[head]

    if head+1==Max:

        head=0

    else:

        head+=1

    return x

q=int(input())

head=0

tail=0

Max=q+1

Q=[0]*(q+1)

T=[list(map(int,input().split())) for i in range(q)]

for t in T:

    if t[0]==1:

        enqueue(t[1])

    elif t[0]==2:

        sentou(t[1])

    else:

        print((Q[tail-t[1]])%Max)
