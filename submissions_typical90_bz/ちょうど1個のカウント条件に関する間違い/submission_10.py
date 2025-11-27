def main():
    N, M = map(int, input().split())
    res_dic = {}

    for _ in range(M):
        a, b = map(int, input().split())
        # aの処理
        if a in res_dic:
            tmp = res_dic[a]
            res_dic[a] = tmp + [b]
        else:
            res_dic[a] = [b]

        # bの処理
        if b in res_dic:
            tmp = res_dic[b]
            res_dic[b] = tmp + [a]
        else:
            res_dic[b] = [a]

    res = 0
    for k, v in res_dic.items():
        count = 0
        for i in v:
            if k > i:
                count += 1
            if count > 1:
                break
        res += 1
    print(res)


if __name__ == "__main__":
    main()
