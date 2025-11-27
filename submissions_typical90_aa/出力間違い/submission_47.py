def main():
  n = int(input())
  s = []
  for i in range(n):
    str = input()
    if (str in s):
      print(i)
    s.append(str)
    