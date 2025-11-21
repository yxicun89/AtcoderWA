# かっこついてないから条件が変になる

def main():

    n, k = map(int, input().split())

    a_list = list(map(int, input().split()))

    b_list = list(map(int, input().split()))

    # print(n,k,a_list, b_list)



    # AとBの各要素の差分を取り、その差がｋと一致したらYes

    # 残り2回動作が残っていても同じ動作を繰り返せば数値の変動なくできる

    # diff = kか、k - diff %2 ==0だったらおっけい

    diff = 0

    for i in range(n):

        diff += abs(a_list[i] - b_list[i])

    if k < diff:

        print("No")

    elif diff == k or k-diff%2 == 0:

        print("Yes")

    else:

        print("No")



if __name__ == "__main__":

    main()

