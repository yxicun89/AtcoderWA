def main(case: str) -> None:
    NK, *ab = case.splitlines()

    N, K = map(int, NK.split())

    # tmp = [tuple(sorted(map(int, x.split()), reverse=True)) for x in ab]

    # ab_list = set(tmp)

    ab_list = [sorted(map(int, x.split()), reverse=True)[0] for x in ab]

    count = 0

    for idx in range(K):
        count += 1
        for idx2 in range(K):
            if idx != idx2 and ab_list[idx] == ab_list[idx]:
                count -= 1
                break

            # if idx == idx2:
            #     continue
            # if ab_list[idx] == ab_list[idx]:
            #     continue

    print(count)


if __file__.endswith("Main.py"):
    import sys

    case: str = "".join([x for x in sys.stdin])
    main(case)