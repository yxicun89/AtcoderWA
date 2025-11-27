def base_n(num_10,n):
    str_n = ''
    while num_10:
        if num_10%n>=10:
            return -1
        str_n += str(num_10%n)
        num_10 //= n
    return str_n[::-1]

num_8, k = input().split()

k = int(k)
cnt = 0
while cnt < k:
    cnt += 1
    num_10 = 0
    for i in range(len(num_8)):
        num_10 += int(num_8[i]) * (8**(len(num_8)-i-1))
        
    num_9 = list(base_n(num_10, 9))
    for i in range(len(num_9)):
        if num_9[i] == '8':
            num_9[i] = '5'
    num_8 = ''.join(num_9)
    
print(num_8)
    