

def input_process() -> tuple[int, list[int], list[int], int, list[int], list[int]]:
    """
    Input process for the problem.

    Returns:
        N (int): Number of elements.
        C (list[int]): List of C values.
        P (list[int]): List of P values.
        Q (int): Number of queries.
        L (list[int]): List of left indices for queries.
        R (list[int]): List of right indices for queries.
    """

    N = int(input())
    C, P = [], []
    for _ in range(N):
        c, p = map(int, input().split())
        C.append(c)
        P.append(p)

    Q = int(input())
    L, R = [], []
    for _ in range(Q):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)

    return N, C, P, Q, L, R


def dp(N, C, P):
    class_1, class_2 = [0] * N, [0] * N
    class_1[0] = P[0] if C[0] == 1 else 0
    class_2[0] = P[0] if C[0] == 2 else 0
    for i in range(1, N):
        if C[i] == 1:
            class_1[i] = class_1[i-1] + P[i]
            class_2[i] = class_2[i-1]
        elif C[i] == 2:
            class_1[i] = class_1[i-1]
            class_2[i] = class_2[i-1] + P[i]
        else:
            raise ValueError("Invalid class value")

    return class_1, class_2


def main():
    N, C, P, Q, L, R = input_process()
    class_1, class_2 = dp(N, C, P)

    for j in range(Q):
        l, r = L[j], R[j]
        ans_1 = class_1[r-1] - class_1[l-2]
        ans_2 = class_2[r-1] - class_2[l-2]
        print(ans_1, ans_2)

main()