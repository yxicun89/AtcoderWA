N = int(input()) 
students_score = []
for _ in range(N):
  student_score = list(map(int, input().split()))
  students_score.append(student_score)
M = int(input())
number_ranges = []
for _ in range(M):
  number_range = list(map(int, input().split()))
  number_ranges.append(number_range)

class1_score = 0
class2_score = 0
for i in range(M):
  n = number_ranges[i][0]
  m = number_ranges[i][1]
  for j in range(n-1,m):
    class_number = students_score[j][0]
    if class_number == 1:
      class1_score += students_score[j][1]
    else:
      class2_score += students_score[j][1]
  result = str(class1_score) + " " + str(class2_score)    
  print(result)
    

#print(students_score)
#print(number_ranges)
  