#生徒データ入力
NUM_STUDENT = int(input())

class1_sum = [0]
class2_sum = [0]
for _ in range(NUM_STUDENT):
    class_id, score = map(int, input().split())
    
    class1_sum.append(class1_sum[-1] + score if class_id == 1 else 0)
    class2_sum.append(class1_sum[-1] + score if class_id == 1 else 0)

#問題データ入力、処理
NUM_QUESTION = int(input())

for _ in range(NUM_QUESTION):
    NUM_LEFT, NUM_RIGHT = map(int, input().split())
    print(class1_sum[NUM_RIGHT]-class1_sum[NUM_LEFT], " ", class2_sum[NUM_RIGHT]-class2_sum[NUM_LEFT])

