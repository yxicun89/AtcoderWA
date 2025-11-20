# 8進数ではなく9進数を表示

def f(n: list[int]) -> list[int]:

    val = 0

    for c in n:

        val *= 8

        val += c



    ans = []

    while val:

        d = val % 9

        ans.append(5 if d == 8 else d)

        val //= 9

    if len(ans) and ans[-1] == 0:

        ans.pop()

    ans.reverse()



    return ans





def solve(n: str, k: int) -> str:

    now = []

    for c in n:

        now.append(int(c))



    for _ in range(k):

        now = f(now)



    return "".join(map(str, now))





n, k = map(str, input().split())

k = int(k)

print(solve(n, k))

