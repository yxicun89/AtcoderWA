
import sys

from sys import stdin

from collections import deque

input = stdin.readline

#入力を受け取る

q=int(input())

#書き出しようのリスト

write_list=[]

#cardのdeque

card_deque=deque()

for i in range(q):

  #入力値を一旦受け取る

  t,x=map(int, input().split())

  if(t==3):

    write_list.append([t,x])

  elif(t==1):

    card_deque.appendleft(x)

  else:

    card_deque.append(x)

#リストに戻す

card_list = list(card_deque)

for tmp in write_list:

  print(card_list[tmp[1]-1])

