h,w = map(int,input().split())

#print(h,w)

a = []

for i in range(h):

    a.append(list(map(int,input().split())))



"""for i in range(h):

    for j in range(w):

        print(a[i][j])"""





# sum

def sum(a,k,l,h,w):

    sum = 0

    for j in range(w):

        #print(j)

        sum += a[k][j]

        #print("sumj = ",sum)

    for i in range(h):

        #print(i)

        sum += a[i][l]

        #print("sumi = ",sum)

    sum -= a[k][l]

    #print(sum)

    return sum

# output



b = []

c = [0]*w

for i in range(h):

    for j in range(w):

        c[j] = sum(a,i,j,h,w)

    b.append(c)



for row in b:

    print(" ".join(map(str, row)))
