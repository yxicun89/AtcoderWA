# setで順序確認でエラー

def main1():

    N = int(input())

    ids = set()

    out = []



    for _ in range(N):

        name = input()

        if not(name in ids):

            ids.add(name)

        else:

            ids.add(None)



    for i, val in enumerate(ids):

        if not(val == None):

            print(i + 1)







main1()
