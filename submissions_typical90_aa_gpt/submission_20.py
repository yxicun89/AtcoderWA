import pandas as pd

N = int(input())
S = [input().strip() for _ in range(N)] 

df = pd.DataFrame([S])
index_list = df.drop_duplicates(keep='first').index.tolist()

for index in index_list:
  print(index + 1)

