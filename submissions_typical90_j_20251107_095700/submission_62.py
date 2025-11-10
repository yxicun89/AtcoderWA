def main():
    n = int(input())
    students = [0] + [list(map(int, input().split())) for i in range(n)]
    sum1 = [0]
    sum2 = [0]
    for i in range(1, n + 1):
        if students[i][0] == 1:
            sum1.append(sum1[-1] + students[i][1])
            sum2.append(sum2[-1])
        if students[i][0] == 2:
            sum1.append(sum1[-1])
            sum2.append(sum2[-1] + students[i][1])
    q = int(input())
    for i in range(q):
        L, R = map(int, input().split())
        print(print_sum(sum1[R], sum1[L - 1]), print_sum(sum2[R], sum2[L - 1]))


def print_sum(R, L):
    res = R - L
    if res == 0:
        return R
    return res


if __name__ == '__main__':
    main()
