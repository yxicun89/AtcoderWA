import numpy as np

def main():
    N = int(input())
    Score = np.array([list(map(int, input().split())) for _ in range(N)])
    Q = int(input())
    Pattern = np.array([list(map(int, input().split())) for _ in range(Q)])
    C1 = np.zeros(N + 1)
    C2 = np.zeros(N + 1)
    for i in range(N):
        if Score[i, 0] == 1:
            C1[i+1] = (Score[i, 1])
        else:
            C2[i+1] = (Score[i, 1])

    for i in range(Q):
        solve_sum(Pattern[i, 0], Pattern[i, 1], C1, C2)


def solve_sum(Left, Right, Score1, Score2):
    nScore1 = Score1[Left:Right+1].sum()
    nScore2 = Score2[Left:Right+1].sum()
    print(nScore1, nScore2)

if __name__ == "__main__":
    main()