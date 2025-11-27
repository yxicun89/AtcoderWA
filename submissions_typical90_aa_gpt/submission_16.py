
# #61923802をもとに辞書でなく集合を使うよう修正



import sys

N = int(input())

name_list = sys.stdin.read().splitlines()[:N]



name_set = set()

for i, name in enumerate(name_list, start=1):

    if not name in name_set:

        print(i)

