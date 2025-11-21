
def main():
    n, m = map(int, input().split())

    a_ = []
    b_ = []
    for _ in range(m):
        a, b = map(int, input().split())
        a_.append(a)
        b_.append(b)
    
    p = [0]*n
    for i in range(m):
        a, b = a_[i], b_[i]
        if a > b:
            p[b] += 1
        else:
            p[a] += 1

    count = 0
    for k in p:
        if k == 1:
            count += 1

    print(count)







if __name__ == "__main__":
    main()