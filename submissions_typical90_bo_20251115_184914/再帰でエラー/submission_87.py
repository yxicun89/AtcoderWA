# 再帰でオーバーフロー

def dec_to_numsystem_str(num, n_str):

  numeral = ""

  n = int(n_str)

  if n == 0:

    numeral = "0"

  else:

    while n > 1:

      n, i = n//num, n%num

      numeral = str(i) + numeral

      if n == 1:

        numeral = str(n) + numeral

  return numeral



def numsystem_to_dec_str(num, numeral_str):

  numeral_list = list(numeral_str)

  numeral_list.reverse()

  dec = 0

  i = 0

  for i, n in enumerate(numeral_list):

    dec += int(n) * (int(num) ** i)

  return str(dec)



n, k = input().split()

for _ in range(int(k)):

  n = dec_to_numsystem_str(9, numsystem_to_dec_str(8, n))

  n = n.replace("8", "5")



print(n)































