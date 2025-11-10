# クエリ処理時の条件が冗長

def main(scores, queries):
    results = []
    cumulative_sum_of_first_class = [0]
    cumulative_sum_of_second_class = [0]
    for idx, (class_number, score) in enumerate(scores):
        if class_number == 1:
            cumulative_sum_of_first_class.append(cumulative_sum_of_first_class[idx]+score)
            cumulative_sum_of_second_class.append(cumulative_sum_of_second_class[idx])
        else:
            cumulative_sum_of_first_class.append(cumulative_sum_of_first_class[idx])
            cumulative_sum_of_second_class.append(cumulative_sum_of_second_class[idx]+score)

    for l, r in queries:
        if r != l and cumulative_sum_of_first_class[r] == cumulative_sum_of_first_class[l]:
            first_class_sum = cumulative_sum_of_first_class[r]
        else:
            first_class_sum = cumulative_sum_of_first_class[r]-cumulative_sum_of_first_class[l-1]
        if r != l and cumulative_sum_of_second_class[r] == cumulative_sum_of_second_class[l]:
            second_class_sum = cumulative_sum_of_second_class[r]
        else:
            second_class_sum = cumulative_sum_of_second_class[r]-cumulative_sum_of_second_class[l-1]
        results.append([first_class_sum, second_class_sum])
    for result in results:
        print(' '.join(map(lambda item: str(item), result)))

if __name__ == '__main__':
    N = int(input())
    scores = [list(map(int, input().split())) for _ in range(N)]
    Q = int(input())
    queries = [list(map(int, input().split())) for _ in range(Q)]
    main(scores, queries)
