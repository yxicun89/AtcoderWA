import sys

def outOfRange(val, minVal, maxVal):
  if(val < minVal or val > maxVal):
    return True
  return False

def main(lines):
  n = int(lines[0])
  q = int(lines[n+1])

  # G = [[] for _ in range(n)] # graph
  # dp = [[0]*(m+1) for _ in range(n+1)] # Dynamic Planning
  list_cp = [] 
  for v in lines[1:n+1]:
    c,p=v.split()
    list_cp.append({"c":int(c), "p":int(p)})
  
  # 学籍番号0からindexまでの点数の合計
  list_sum_c1 = []
  list_sum_c2 = [] 
  sum_c1,sum_c2 = 0,0
  for i in range(n):
    if(list_cp[i]["c"]==1): 
      sum_c1 += list_cp[i]["p"]
    else:
      sum_c2 += list_cp[i]["p"]
    list_sum_c1.append(sum_c1)
    list_sum_c2.append(sum_c2)

  for v in lines[-q:]:
    left,right=list(map(int,v.split()))
    ans_c1 = list_sum_c1[right-1]-list_sum_c1[left-1]
    ans_c2 = list_sum_c2[right-1]-list_sum_c2[left-1]
    print(f"{ans_c1} {ans_c2}")


if __name__ == '__main__':
  lines = []
  for l in sys.stdin:
    lines.append(l.rstrip('\r\n'))
  main(lines)     
