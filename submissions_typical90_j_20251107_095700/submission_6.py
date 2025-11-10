#関数をコメントしてる

from typing import List, Tuple
def scoreSumQueries(N: int, student: List[Tuple[int,int]], Q: int, queries: List[Tuple[int,int]]) -> List[Tuple[int,int]]:
  # class1 = [0] * (N + 1)
  # class2 = [0] * (N + 1)
  # for i, std in enumerate(student):
  #   cl, score = std
  #   class1[i+1] = class1[i]
  #   class2[i+1] = class2[i]
  #   if cl == 1:
  #     class1[i+1] += score
  #   elif cl == 2:
  #     class2[i+1] += score
  
  ans = []
  # for query in queries:
  #   left, right = query
  #   score1 = class1[right] - class1[left-1]
  #   score2 = class2[right] - class2[left-1]
  #   ans.append((score1, score2))
  
  return ans

def main():
  N = int(input())
  student = []
  for _ in range(N):
    cl, score = map(int, input().split())
    student.append((cl, score))
    
  Q = int(input())
  query = []
  for _ in range(Q):
    left, right = map(int, input().split())
    query.append((left, right))
  
  scores = scoreSumQueries(N, student, Q, query)
  for score in scores:
    c1, c2 = score
    print(f"{c1} {c2}")

if __name__ == "__main__":
  main()
  