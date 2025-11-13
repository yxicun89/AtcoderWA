def process_deck_operations_from_input():
    Q = int(input().strip())  # Number of operations
    deck = []

    for _ in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            deck.insert(0, x)
        elif t == 2:
            deck.append(x)
        elif t == 3:
            print(deck[x - 1])

# To run the program, call `process_deck_operations_from_input()` and provide the input in the specified format
