import sys

def outOfRange(val, minVal, maxVal):
  if(val < minVal or val > maxVal):
    return True
  return False

def base8StrToBase10(n_str):
  result = 0
  for i in range(len(n_str)):
    digit = int(n_str[-i-1])
    result += digit * (8**i)
  return result

def base10ToNextStr(n_int):
  result = ""
  while n_int>0:
    digit = n_int%9
    if(digit==8): digit = 5
    result = str(digit)+result
    n_int = n_int//9
  return result

def main(lines):
  n_str,k_str = lines[0].split()
  k = int(k_str)
  # G = [[] for _ in range(n)] # graph
  # dp = [[0]*(m+1) for _ in range(n+1)] # Dynamic Planning

  for _ in range(k):
    base10 = base8StrToBase10(n_str)
    n_str = base10ToNextStr(base10)

  print(n_str)


if __name__ == '__main__':
  lines = []
  for l in sys.stdin:
    lines.append(l.rstrip('\r\n'))
  # lines = ["2311640221315 15"]
  main(lines)     
