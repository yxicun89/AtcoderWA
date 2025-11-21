A,B,C = map(int, input().split())

def gcd_t(list):
    for i in reversed(range(1, min(list)+1)):
        for j in list:
            if j%i != 0:
                break
            else:
                return i
            
cut = gcd_t([A,B,C])
sum = A//cut + B//cut + C//cut

print(sum)